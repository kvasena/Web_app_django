from django.shortcuts import render
from .models import *


def post_list(request):
    posts = Post.objects.order_by('updated')

    return render(request, 'blog/post_list.html', {'posts': posts})
