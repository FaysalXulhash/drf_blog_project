from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
# Create your views here.


class PostListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
