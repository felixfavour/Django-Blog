from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.filter(author=User.objects.get(username='chinemerem')).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
