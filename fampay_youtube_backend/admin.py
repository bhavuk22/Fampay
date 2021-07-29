from django.contrib import admin

from fampay_youtube_backend import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['publish_date_time', 'video_id', 'channel_id',
                    'title']
    search_fields = ('publish_date_time', 'video_id', 'channel_id',
                     'title')
    list_filter = ('publish_date_time',)


@admin.register(models.VideoThumbNail)
class VideoThumbNailAdmin(admin.ModelAdmin):
    list_display = ['video', 'id']
    search_fields = ('video', 'id')
    list_filter = ('video', 'screen_size')


@admin.register(models.APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['key', 'is_limit_over']
