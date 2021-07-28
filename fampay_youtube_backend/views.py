from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from fampay_youtube_backend import serializers


class AddAPIKey(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.APIKeySerializer
