from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer

from fampay_youtube_backend import serializers, models


class GetVideos(generics.ListAPIView):
    """View for getting all the videos, order by latest published date."""
    renderer_classes = [JSONRenderer]
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    serializer_class = serializers.VideoSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        api_keys = models.APIKey.objects.filter(is_limit_over=False)
        if not len(api_keys):
            raise ValidationError("All APIKey's Expired, Add a new APIKey")
        return models.Video.objects.all().order_by('-publish_date_time')


class AddAPIKey(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.APIKeySerializer
