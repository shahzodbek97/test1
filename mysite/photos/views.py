from .models import Category, Photo
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Category
    template_name = 'list.html'
    context_object_name = 'category'


class HomeListView(ListView):
    model = Photo
    template_name = 'home.html'
    context_object_name = 'photo'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'detail.html'
    context_object_name = 'det'
