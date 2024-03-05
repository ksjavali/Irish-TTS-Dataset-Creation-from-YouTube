from pathlib import Path
import shutil
import spacy
import stopwordsiso as stopwords
from src.config import ORGANIZED_DIR, RESULTS_DIR

# Initialize NLP tools
nlp = spacy.blank("ga")
irish_stopwords = stopwords.stopwords("ga")

def normalize_text(text, nlp, irish_stopwords):
    doc = nlp(text)
    filtered_tokens = [token.text for token in doc if token.text not in irish_stopwords and not token.is_punct]
    return " ".join(filtered_tokens)

def organize_files(video_id, src_dir, dest_dir):
    # Ensure destination directory exists
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Move all files for video_id to its folder
    for file in src_dir.glob(f"{video_id}*"):
        shutil.move(str(file), dest_dir / file.name)

def process_text():
    for dir_path in ORGANIZED_DIR.iterdir():
        if dir_path.is_dir():
            video_id = dir_path.name
            result_video_dir = RESULTS_DIR / video_id
            result_video_dir.mkdir(parents=True, exist_ok=True)  # Create directory for video ID in results
            
            for txt_file_path in dir_path.glob("*.txt"):
                with open(txt_file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                # Process text and organize files
                if "[Ceol]" not in text:
                    normalized_text = normalize_text(text, nlp, irish_stopwords)
                    normalized_file_path = result_video_dir / f"{txt_file_path.stem}_normalized.txt"
                    with open(normalized_file_path, "w", encoding="utf-8") as nf:
                        nf.write(normalized_text)
                    
                    # Also move the original .txt and corresponding .wav to the result directory
                    shutil.move(str(txt_file_path), result_video_dir / txt_file_path.name)
                    wav_file_path = dir_path / f"{txt_file_path.stem}.wav"
                    if wav_file_path.exists():
                        shutil.move(str(wav_file_path), result_video_dir / wav_file_path.name)
                    
                    print(f"Processed and saved files for {video_id}.")
                else:
                    # Delete files directly if "[Ceol]" is found
                    txt_file_path.unlink()
                    wav_file_path = dir_path / f"{txt_file_path.stem}.wav"
                    if wav_file_path.exists():
                        wav_file_path.unlink()

    print("Processing and organization complete.")
