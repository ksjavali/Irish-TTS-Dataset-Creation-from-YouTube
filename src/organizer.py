import os
import shutil
from src.config import ORGANIZED_DIR, AUDIO_FILES_DIR, TRANSCRIPTS_DIR

def organize_files(video_ids):
    os.makedirs(ORGANIZED_DIR, exist_ok=True)
    for video_id in video_ids:
        video_id_dir = os.path.join(ORGANIZED_DIR, video_id)
        os.makedirs(video_id_dir, exist_ok=True)
        audio_file_path = os.path.join(AUDIO_FILES_DIR, f"{video_id}.wav")
        if os.path.exists(audio_file_path):
            shutil.move(audio_file_path, os.path.join(video_id_dir, os.path.basename(audio_file_path)))
        transcript_file_path = os.path.join(TRANSCRIPTS_DIR, f"{video_id}.json")
        if os.path.exists(transcript_file_path):
            shutil.move(transcript_file_path, os.path.join(video_id_dir, os.path.basename(transcript_file_path)))
    print("Files have been organized.")
