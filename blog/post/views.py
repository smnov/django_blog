from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def home(request):
    posts = Post.objects.all()
    return HttpResponse(request, 'Hello')
    # return render(request, 'home.html', context={'posts': posts})