from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer
from app.permissions import GlobalDefaultPermission




# Create your views here.

class MoviesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset= Movie.objects.all()
    serializer_class = MovieSerializer