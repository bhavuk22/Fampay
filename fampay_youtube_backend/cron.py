from urllib.error import HTTPError

from googleapiclient.discovery import build

from fampay_youtube_backend import models
import datetime

from fampay_youtube_backend.models import Video


def fetch_and_store_youtube_videos():
    print(datetime.datetime.now(datetime.timezone.utc))
    api_keys = models.APIKey.objects.filter(is_limit_over=False)
    print(api_keys)
    if not len(api_keys):
        print("NO API KEY FOUND")
    DEVELOPER_KEY = api_keys[0]
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    try:
        youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                               developerKey=DEVELOPER_KEY)
        new_interval_start_time = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
            minutes=5)
        new_interval_start_time_string = str(new_interval_start_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        data = youtube_object.search().list(q='music', part="id,snippet", type="video", order="date",
                                            publishedAfter=new_interval_start_time_string,
                                            maxResults=10).execute()
        print(data)
        for video in data["items"]:
            publish_date_time = str(video["snippet"]["publishedAt"])
            publish_date_time = datetime.datetime.strptime(publish_date_time, '%Y-%m-%dT%H:%M:%SZ')
            title = str(video["snippet"]["title"])
            description = str(video["snippet"]["description"])
            channel_id = str(video["snippet"]["channelId"])
            video_id = str(video['id']['videoId'])

            video_db = Video.objects.create(
                publish_date_time=publish_date_time,
                title=title,
                description=description,
                channel_id=channel_id,
                video_id=video_id
            )

            thumbnails = get_video_thumbnails_from_youtube_data(video)
            for thumbnail in thumbnails:
                thumbnail['video'] = video_db
                thumbnail_obj = models.VideoThumbNail(**thumbnail)
                thumbnail_obj.save()
    except HTTPError as ex:
        api_keys[0].is_limit_over = True
        api_keys[0].save()
        print(ex)
    except Exception as ex:
        print(ex)


def get_video_thumbnails_from_youtube_data(data):
    return [{
        'screen_size': screen_size,
        'url': data['snippet']['thumbnails'][screen_size]['url'],
    } for screen_size in data['snippet']['thumbnails']]
