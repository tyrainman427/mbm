from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from mublog.sitemaps import PostSitemap
from .feeds import LatestPostsFeed

app_name = 'mublog'

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]
