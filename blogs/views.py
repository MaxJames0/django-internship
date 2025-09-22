from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView

from blogs.models import Blog

# Create your views here.

# class BlogList(TemplateView):
#     template_name = "./blogs/blogs.html"
    
class BlogList(ListView):
    template_name = "./blogs/blogs.html"
    model = Blog
    context_object_name = 'blogs'
    
    
class BlogDetail(DetailView):
    model = Blog
    template_name = './blogs/detail.html'
    context_object_name = 'blog'
    
class BlogDashboardList(ListView):
    template_name = './blogs/blog_list_dashboard.html'
    model = Blog
    context_object_name = 'blogs'