from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

class HomePage(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "all_post_list"