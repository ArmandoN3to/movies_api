from django.urls import path
from . import views

urlpatterns = [ 
    path('actors/',views.ActorsListCreateView.as_view(),name='actors_create_list'),
    path('actors/<int:pk>/',views.ActorsRetrieveUpdateDestroyView.as_view() ,name='actor_detail'),
    ]