from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.


class homeview(ListView):
    model = Blog
    template_name = "home.html"
    context_object_name = "blog_list"


class detailview(DetailView):
    model = Blog
    template_name = "detail.html"
    context_object_name = "object"
