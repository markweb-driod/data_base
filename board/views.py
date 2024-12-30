from django.shortcuts import render
from django.views.generic import ListView
from .models import post

# Create your views here.
class Hello(ListView):
    model = post
    template_name = 'index.html'
    context_object_name = 'all_post'