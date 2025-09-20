from django.urls import path, include
from .views import  BlogList , BlogDetail

app_name = 'blog'

urlpatterns = [
    path('' , BlogList.as_view() , name="list-blog"),
    path('/<int:pk>/<slug:slug>' , BlogDetail.as_view() , name="detail-blog"),
 
]
