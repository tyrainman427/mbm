from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member, Address, Membership
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from mublog.models import Post
from .forms import MemberUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


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
    model = Address
    queryset = Member.objects.all()
    address = Address.objects.all()
    template_name = 'members/member_list.html'


class MemberDetailView(DetailView):
    template_name = "members/member_detail.html"
    member = Member.objects.all()
    form_class = MemberUpdateForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Member, id=id_)

    def form_valid(self,form):
        return super().form_valid(form)


class MemberCreateView(CreateView):
    model = Member
    fields = ['first_name', 'last_name','phone_number','email_address',
    ]
    
@login_required
class MemberUpdateView(UpdateView):
    model = Member
    fields = ['first_name', 'last_name','email_address',
    ]

class MemberDeleteView(DeleteView):
    model = Member
    success_url = '/members/'

