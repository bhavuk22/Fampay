from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer


class AddAPIKey(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.APIKeySerializer
