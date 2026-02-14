
from django.http import Http404

from rest_framework.views import APIView  #genericview&listapiview
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from .models import Post
from .serializer import PostSerializer


class postListview(generics.ListCreateAPIViewAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class postDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

