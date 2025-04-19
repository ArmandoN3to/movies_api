"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView , GenreRetrieveUpdateDestroyView 
from actors.views import ActorsListCreateView , ActorsRetrieveUpdateDestroyView
from movies.views import MoviesCreateListView , MoviesRetrieveUpdateDestroyView

urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('genres/',GenreListCreateView.as_view(), name='genre_create_list'),  # URL for the genre list view
    path('genres/<int:pk>/',GenreRetrieveUpdateDestroyView.as_view() ,name='genre_detail'),

    path('actors/',ActorsListCreateView.as_view(),name='actors_create_list'),
    path('actors/<int:pk>/',ActorsRetrieveUpdateDestroyView.as_view() ,name='actor_detail'),
    
    path('movies/',MoviesCreateListView.as_view(),name='movies_create_list'),
    path('movies/int:pk>/',MoviesRetrieveUpdateDestroyView.as_view(),name='movie_detail'),
]
