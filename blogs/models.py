from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

Users = get_user_model()

class Blog(models.Model):
    title = models.CharField(verbose_name='عنوان' , max_length=255)
    slug = models.SlugField(unique = True)
    desc = models.TextField(verbose_name='توضیحات کوتاه')
    # todo insert catergory
    user = models.ForeignKey(Users , on_delete=models.CASCADE , verbose_name='کاربر')
    content = models.TextField(verbose_name='توضیحات کامل')
    img = models.ImageField(upload_to='./uploads')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} | {self.user}'
    
    
    
