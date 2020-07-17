from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member, Tweet, Follow
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from mublog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    post = Post.objects.filter(status=1).order_by('-created_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 2)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {'post':post}
    return render(request,'members/index.html',context)

# class FollowView(CreateView):
#     form_class = FollowForm
#     model = Follow
#     success_url = reverse_lazy('timeline_feed')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(FollowView, self).form_valid(form)


class UnfollowView(DeleteView):
    model = Follow
    success_url = reverse_lazy('timeline_feed')

    def get_object(self):
        target_id = self.kwargs['target_id']
        return self.get_queryset().get(target__id=target_id)

from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

enricher = Enrich()


class UserView(DetailView):
    model = User
    template_name = 'stream_twitter/user.html'

    def get_object(self):
        return self.get_queryset().get(username=self.kwargs['username'])

    def get_context_data(self, object):
        user = self.object
        feeds = feed_manager.get_user_feed(user.id)
        activities = feeds.get()['results']
        activities = enricher.enrich_activities(activities)

        return {
            'activities': activities,
            'user': user,
            'login_user': self.request.user
        }

class TweetView(CreateView):
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)

class TimelineView(TemplateView):
    template_name = 'stream_twitter/timeline.html'

    def get_context_data(self):
        context = super(TimelineView, self).get_context_data()

        feeds = feed_manager.get_news_feeds(self.request.user.id)
        activities = feeds.get('timeline').get()['results']
        enriched_activities = enricher.enrich_activities(activities)

        context['activities'] = enriched_activities

        return context

def about(request):
    return render(request, 'members/about.html')

def contact(request):
    return render(request, 'members/contact.html')

def signup(request):
    return render(request, 'members/member_signup.html')

def employee_portal(request):
    return render(request,'employee/index.html')

class MemberList(ListView):
    model = Member
    queryset = Member.objects.all()
    template_name = 'members/member_list.html'

    def get_queryset(self):
        result = super(MemberList, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(first_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(email_address__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(city__icontains=q) for q in query_list))
            )

        return result

class MemberDetailView(DetailView):
    template_name = "members/member_detail.html"
    member = Member.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Member, id=id_)


class MemberCreateView(CreateView):
    model = Member
    fields = ['first_name', 'last_name','address','city',
    'state','zip','phone_number','email_address',
    ]

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['first_name', 'last_name','address','city',
    'state','zip','phone_number','email_address',
    ]

    def get_absolute_url(self): # new
        return reverse('members:members_detail', args=[str(self.id)])

class MemberDeleteView(DeleteView):
    model = Member
    success_url = '/members/'
