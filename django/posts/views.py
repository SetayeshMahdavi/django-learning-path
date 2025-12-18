from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Comment
def index (request):
    return HttpResponse("<h1> welcom to Django .sety </h1>")

def home (request):
    return HttpResponse("<h1> hi you are in home.</h1>")


def post_list (request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'posts/post_list.html',context=context)


def post_detail(request,post_id):
    post=Post.objects.get(pk=post_id)
    comments=Comment.objects.filter(post=post)
    context={'post':post,'comment':comments}
    return render(request, 'posts/post_detail.html' ,context=context)
