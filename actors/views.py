from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer

# Create your views here.
class ActorsListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer 


class ActorsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset= Actor.objects.all()
    serializer_class = ActorSerializer