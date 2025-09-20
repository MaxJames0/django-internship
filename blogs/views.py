from django.shortcuts import render
from django.views.generic import TemplateView , ListView

from blogs.models import Blog

# Create your views here.

# class BlogList(TemplateView):
#     template_name = "./blogs/blogs.html"
    
class BlogList(ListView):
    template_name = "./blogs/blogs.html"
    model = Blog
    
    