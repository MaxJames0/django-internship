from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

Users = get_user_model()


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='دسته بندی')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='ساخته شده در')
    status = models.BooleanField(default=True , verbose_name='وضعیت نمایش')
    
    def __str__(self):
        return f'{self.name}'



class Blog(models.Model):
    title = models.CharField(verbose_name='عنوان' , max_length=255)
    slug = models.SlugField(unique = True)
    desc = models.TextField(verbose_name='توضیحات کوتاه')
    category = models.ForeignKey(BlogCategory, blank=True , null=True , on_delete=models.CASCADE , related_name='category' , verbose_name='دسته بندی')
    user = models.ForeignKey(Users , on_delete=models.CASCADE , verbose_name='کاربر')
    content = models.TextField(verbose_name='توضیحات کامل')
    img = models.ImageField(upload_to='./uploads')
    status = models.BooleanField(default=True , verbose_name='وضعیت نمایش')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='ساخته شده در')
    updated_at = models.DateTimeField(auto_now=True , verbose_name='بروز شده در')
    
    def __str__(self):
        return f'{self.title} | {self.user}'
    
    
