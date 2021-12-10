from .models import Post
from django.views import generic
from django.shortcuts import render
# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'