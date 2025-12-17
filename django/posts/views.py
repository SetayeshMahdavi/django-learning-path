from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def index (request):
    return HttpResponse("<h1> welcom to Django .sety </h1>")

def home (request):
    return HttpResponse("<h1> hi you are in home.</h1>")


def post_list (request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'posts/post_list.html',context=context)

