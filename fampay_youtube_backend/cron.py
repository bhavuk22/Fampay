from googleapiclient.discovery import build

from fampay_youtube_backend import models
import datetime

from fampay_youtube_backend.models import Video


def fetch_and_store_youtube_videos():
    api_keys = models.APIKey.objects.filter(is_limit_over=False)
    if not len(api_keys):
        raise Exception("NO API KEY FOUND")
    DEVELOPER_KEY = api_keys[0]
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    try:
        youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                               developerKey=DEVELOPER_KEY)
        new_interval_start_time = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
            minutes=5)
        new_interval_start_time_string = str(new_interval_start_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        data = youtube_object.search().list(q='news', part="snippet", type="video", order="date",
                                            publishedAfter=new_interval_start_time_string,
                                            maxResults=10).execute()

        for video in data["items"]:
            published_at = str(video["snippet"]["publishedAt"])
            published_at = datetime.datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
            title = str(video["snippet"]["title"])
            description = str(video["snippet"]["description"])
            channel_title = str(video["snippet"]["channelTitle"])
            thumbnail_url = str(video["snippet"]["thumbnails"]["default"]["url"])

            # Create Object
            Video.objects.create(
                published_at=published_at,
                title=title,
                description=description,
                channel_title=channel_title,
                thumbnail=thumbnail_url)

    except Exception:
        api_keys[0].is_limit_over = True
        api_keys[0].save()
        raise Exception("API KEY EXPIRED")
