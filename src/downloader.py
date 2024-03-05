from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi
import json
from src.config import AUDIO_FILES_DIR, TRANSCRIPTS_DIR
import os

def download_audio(video_urls):
    audio_download_options = {
        'format': 'bestaudio/best',
        'outtmpl': AUDIO_FILES_DIR + '/%(id)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', 'preferredquality': '192'}],
        'quiet': False
    }
    with YoutubeDL(audio_download_options) as ydl:
        ydl.download(video_urls)

def download_transcripts(video_ids):
    # Ensure the transcripts directory exists
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

    for video in video_ids:
        output_file_path = os.path.join(TRANSCRIPTS_DIR, f"{video}.json")
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video)
            transcript = transcript_list.find_transcript(['en']).translate('ga').fetch()
            transcript_json = json.dumps(transcript, ensure_ascii=False, indent=4)
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(transcript_json)
            print(f"Transcript saved to {output_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
