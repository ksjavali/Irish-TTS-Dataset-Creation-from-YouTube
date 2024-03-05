from src.youtube import search_videos
from src.downloader import download_audio, download_transcripts
from src.organizer import organize_files
from src.audio_processor import process_audio_segments
from src.text_processor import process_text

if __name__ == '__main__':
    query = "Gaeilge i mo chroí"
    video_ids = search_videos(query)
    print(f"Found {len(video_ids)} videos with Irish subtitles.")
    video_urls = [f"https://www.youtube.com/watch?v={id}" for id in video_ids]
    
    download_audio(video_urls)
    download_transcripts(video_ids)
    organize_files(video_ids)
    process_audio_segments()
    process_text()
    print("All processing complete.")
