from django.conf.urls import url

from .views import PostList, PostDetail

app_name = 'blog'

urlpatterns = [
    url(r'^$', PostList.as_view(), name="post-list"),
    # url(r'^simple-view/$', SimpleView.as_view(), name="simple-view"),
    url(r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), name="post-detail"),

]


