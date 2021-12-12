from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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


class newview(CreateView):
    model = Blog
    template_name = "newview.html"
    fields = ['title', 'author', 'body']


class editview(UpdateView):
    model = Blog
    template_name = "edit.html"
    fields = ['title', 'body']


class deleteview(DeleteView):
    model = Blog
    template_name = "delete.html"
    context_object_name = "blog"
    success_url = reverse_lazy('home')
