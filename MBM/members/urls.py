from django.urls import path
from django.urls import re_path
from .views import MemberList, MemberDetailView, index, MemberCreateView, MemberUpdateView, MemberDeleteView, signup,about,contact, employee_portal
from django.contrib.auth.decorators import login_required
from members import views

app_name = 'members'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('about/', about, name='about'),
    path('contact/', contact,name='contact'),
    path('members/', MemberList.as_view(), name='member-list'),
    path('<int:id>/', MemberDetailView.as_view(), name='members_detail'),
    path('create/', MemberCreateView.as_view(), name='member-create'),
    path('members/<pk>/update/', MemberUpdateView.as_view(), name='member-update'),
    path('members/<pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),

    path('portal/', employee_portal, name='portal'),
    path('timeline/', login_required(views.TimelineView.as_view()), name='timeline'),
    re_path(r'^user/(?P<username>.+)/', views.UserView.as_view(), name='user_feed')

]
