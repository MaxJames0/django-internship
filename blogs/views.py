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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        next_post = Blog.objects.filter(
            created_at__gt=blog.created_at, status=True
        ).order_by('created_at').first()

        previous_post = Blog.objects.filter(
            created_at__lt=blog.created_at, status=True
        ).order_by('-created_at').first()
        
        context['next_post'] = next_post
        context['previous_post'] = previous_post
        return context
    

class BlogDashboardList(ListView):
    template_name = './blogs/blog_list_dashboard.html'
    model = Blog
    context_object_name = 'blogs'