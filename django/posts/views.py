from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect,HttpResponseNotFound
from .models import Post,Comment
from .forms import PostForm
from django.views import generic




def index (request):
    return HttpResponse("<h1> welcom to Django .sety </h1>")

def home (request):
    return HttpResponse("<h1> hi you are in home.</h1>")


# def post_list (request):
#     posts=Post.objects.all()
#     context={'posts':posts}
#     return render(request,'posts/post_list.html',context=context)

class Postlist(generic.ListView):
    queryset=Post.objects.all()
    template_name='posts/post_list.html'
    context_object_name='posts'

def post_detail(request,post_id):
    # try:    
    #     post=Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound("post is not exist")
    post=get_object_or_404(Post,pk=post_id)
    comments=Comment.objects.filter(post=post)
    context={'post':post,'comment':comments}
    return render(request, 'posts/post_detail.html' ,context=context)


class PostDetail(generic.DetailView):
    model=Post
    template_name='posts/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context= super(PostDetail ,self).get_context_data(**kwargs)
        context['Comment']=Comment.objects.filter(post=kwargs['object'].pk)
        return context

def post_create(request):
    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect ('/posts/')
        
        form=PostForm()
        context={'form':form}
    return render(request,'posts/post_create.html',context=context,)