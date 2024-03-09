from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('authors/title_details/<int:id>', views.details, name='details'),
    
]