from django.contrib import admin
from django.urls import path, include
from home import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('thanks', views.thanks, name='thanks'),
    path('puzzle/nurikabe/<int:id>', views.nurikabe, name='nurikabe'),
    path('puzzle/tat/', TemplateView.as_view(template_name='tat.html  '),
         name='nurikabe'),
]
