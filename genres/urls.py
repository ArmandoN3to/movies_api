from django.urls import path
from . import views

urlpatterns = [ 
    path('genres/',views.GenreListCreateView.as_view(), name='genre_create_list'),  # URL for the genre list view
    path('genres/<int:pk>/',views.GenreRetrieveUpdateDestroyView.as_view() ,name='genre_detail'),
    ]