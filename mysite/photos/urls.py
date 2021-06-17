from django.urls import path
from .views import CategoryListView, HomeListView, PhotoDetailView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('list/', CategoryListView.as_view(), name='list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='detail'),
]
