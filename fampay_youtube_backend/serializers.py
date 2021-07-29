from rest_framework import serializers

from fampay_youtube_backend import models


class VideoSerializer(serializers.ModelSerializer):
    thumbnails = serializers.SerializerMethodField()

    def get_thumbnails(self, obj):
        return [
            VideoThumbNailSerializer(thumbnail).data
            for thumbnail in models.VideoThumbNail.objects.filter(video=obj)]

    class Meta:
        model = models.Video
        fields = '__all__'


class VideoThumbNailSerializer(serializers.ModelSerializer):
    """Serializer for VideoThumbNail Model."""

    class Meta:
        model = models.VideoThumbNail
        fields = '__all__'


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.APIKey
        fields = '__all__'
