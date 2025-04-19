from django.shortcuts import render
from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer



# Create your views here.

class MoviesCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Movie.objects.all()
    serializer_class = MovieSerializer