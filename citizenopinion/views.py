from django.shortcuts import render
from . import models 
from .models import Post


def home_page(request):
    posts = Post.objects.all().order_by('-create_date')
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


