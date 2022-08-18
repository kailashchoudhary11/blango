from blog.views import index, post_detail
from django.urls import path

app_name = "blog"

urlpatterns = [
  path("", index, name="index"),
  path("post/<slug:slug>", post_detail, name="blog-post-detail"),
]