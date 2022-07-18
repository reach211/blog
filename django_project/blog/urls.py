from django.urls import path
from .views import *

urlpatterns = [
    path("post/delete/<int:pk>/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/edit/<int:pk>/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),  # new
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
]