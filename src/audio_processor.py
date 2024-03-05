from pydub import AudioSegment
import json
from src.config import ORGANIZED_DIR
import os

def process_audio_segments():
    for video_id in os.listdir(ORGANIZED_DIR):
        dir_path = os.path.join(ORGANIZED_DIR, video_id)
        if os.path.isdir(dir_path):  # Make sure it's a directory
            for file in os.listdir(dir_path):
                if file.endswith(".wav"):  # Check for audio files
                    audio_file_path = os.path.join(dir_path, file)
                    base_name = os.path.splitext(file)[0]

                    # Assuming the transcript file has the same base name but with a .json extension
                    transcript_file_path = os.path.join(dir_path, f"{base_name}.json")

                    # Proceed only if both audio and transcript files exist
                    if os.path.exists(transcript_file_path):
                        # Load the audio file
                        audio = AudioSegment.from_file(audio_file_path)

                        # Load the transcript data from the JSON file
                        with open(transcript_file_path, 'r', encoding='utf-8') as f:
                            transcript_data = json.load(f)

                        # Process each transcript entry
                        for i, entry in enumerate(transcript_data):
                            # Calculate the start and end times in milliseconds
                            start_time = int(entry['start'] * 1000)
                            end_time = int((entry['start'] + entry['duration']) * 1000)
                            
                            # Extract the audio segment
                            segment = audio[start_time:end_time]
                            
                            # Define the base filename for the audio and transcript files
                            segment_filename = f"{base_name}_{i:03d}"
                            
                            # Save the audio segment
                            segment_path = os.path.join(dir_path, f"{segment_filename}.wav")
                            segment.export(segment_path, format="wav")
                            
                            # Save the corresponding transcript text
                            transcript_path = os.path.join(dir_path, f"{segment_filename}.txt")
                            with open(transcript_path, 'w', encoding='utf-8') as f:
                                f.write(entry['text'])

    print("Audio segments and transcripts have been saved.")
