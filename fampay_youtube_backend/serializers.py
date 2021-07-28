from rest_framework import serializers

from fampay_youtube_backend import models


class APIKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.APIKey
        fields = '__all__'
