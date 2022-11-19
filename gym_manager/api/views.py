from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
