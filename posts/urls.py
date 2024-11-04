from django.urls import path
from .views import PostListApi, PostDetailApi

urlpatterns = [
    path('', PostListApi.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailApi.as_view(), name='post-detail'),
]