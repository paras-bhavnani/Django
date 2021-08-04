from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

@login_required
def blogger(request, userId):
    authors = Author.objects.get(id__exact = userId)
    posts = Post.objects.filter(author__id = userId)
    posts = posts.order_by('-date')
    return render(request, 'blogger.html', {'author': authors, 'userId':userId, 'posts': posts})

@login_required
def blogID(request, blogId):
    #authors = Author.objects.get(id__exact = userId)
    posts = Post.objects.get(id__exact = blogId)
    #posts = posts.order_by('-date')
    return render(request, 'blogID.html', {'posts': posts})
    
@login_required
def bloggers(request):
    authors = Author.objects.all()
    #posts = Post.objects.get(id__exact = blogId)
    #posts = posts.order_by('-date')
    return render(request, 'bloggers.html', {'authors': authors})
