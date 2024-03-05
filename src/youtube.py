from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.config import DEVELOPER_KEY

def search_videos(query, max_results=100):
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    try:
        search_response = youtube.search().list(q=query, part='id', type='video', maxResults=max_results).execute()
        video_ids = [item['id']['videoId'] for item in search_response['items']]
        return video_ids
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
        return []
