from django.urls import path
from . import views
from .views import members  # Import the members view function

urlpatterns = [

    path('members/', members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('search/', views.search_results, name='search_results'),
    path('remaining-authors/', views.remaining_authors, name='remaining_authors'),

    # Add other URL patterns as needed
]