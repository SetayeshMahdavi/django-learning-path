from rest_framework.views import APIView  #genericview&listapiview
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from rest_framework.decorators import api_view

from .serializer import PostSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
