from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Post,Comment
from .forms import PostForm




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


def post_create(request):
    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect ('/posts/')

    else:
        form=PostForm()
        context={'form':form}
    return render(request,'posts/post_create.html',context=context,)