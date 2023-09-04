pip install --upgrade google-api-python-client
from googleapiclient.discovery import build
import googleapiclient.discovery
from pprint import pprint
import pymongo

api_key = 'AIzaSyBzoyrBAtmnFTqty0m3JwL9wLFdY8QmRl0'

api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
       api_service_name, api_version, developerKey=api_key)


request = youtube.channels().list(
       id="UC2J_VKrAzOEJuQvFFtj3KUw",
        part="snippet,contentDetails,statistics",

    )
response = request.execute()

channel_details = dict(channel_id = response['items'][0]['id'],
                       channel_name = response['items'][0]['snippet']['title'],
                       channel_description = response['items'][0]['snippet']['description'],
                       channel_sudscriberCount = response['items'][0]['statistics']['subscriberCount'],
                       channel_view_count = response['items'][0]['statistics']['viewCount'],
                       channel_video_count = response['items'][0]['statistics']['videoCount'],
                       channel_publish_date = response['items'][0]['snippet']['publishedAt'],
                       playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
                       )

playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

request = youtube.playlistItems().list(
        part="snippet,contentDetails,statistics",
        playlistId = playlist_id,
        maxResult=50
    )
response = request.execute()


video_ids = []
for item in response ['items']:
  video_id = item['contentDetails']['videoId']
  print(video_id)
  video_ids.append(video_id)
