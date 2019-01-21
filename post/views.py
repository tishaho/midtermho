from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm
from .forms import CommentForm
from django.utils import timezone

# Create your views here.


def index(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'index.html', context)

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Post updated')
        else:
            context['form'] = form
            return render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
        return render(request, 'update.html', context)

def comment(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return HttpResponse('Comment added')
        else:
            context['form'] = form
            return render(request, 'comment.html', context)
    else:
        context['form'] = CommentForm(instance=post)
        return render(request, 'comment.html', context)


def create(request):

    context = {}
    form = PostModelForm(initial={"date_created":timezone.now()})

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:index')

    return render(request, 'create.html', {'form': form})
