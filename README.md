# Data Science project: Irish TTS Dataset Creation from YouTube

## Introduction:
This project aims to design and implement a data engineering pipeline specifically focused on the creation of a Text-to-Speech (TTS) dataset for the Irish language, leveraging publicly available content on YouTube. The significance of this work lies in its potential to enrich TTS technologies with high-quality, diverse datasets in less-represented languages such as Irish, contributing to the preservation and digital accessibility of these languages.


## Methodology:
The pipeline comprises several stages, each tailored to handle specific aspects of data acquisition, processing, and refinement. Here&#39;s an outline of my approach:
1. Video Identification: The first step was to identify videos with Gaelic content with Gaelic subtitles. This task was challenging as there are videos in Gaelic available, but there were very few with Gaelic subtitles as well. While researching, I came across an Irish vlogger, who vlogs in Gaelic, and has enabled subtitles in Gaelic as well. Hence, the YouTube API was utilized to search for videos based on queries related to the Irish
language and the vlogger’s channel. This step ensures a targeted collection of videos likely to contain relevant content.
2. Audio and Transcript Download: For each identified video, the audio track was downloaded using yt-dlp, a command-line program to download videos from YouTube and other video sites. Concurrently, the video&#39;s transcript were fetched using the YouTube Transcript API, translating it into Irish (ga) when necessary.
3. Data Organization: To create a directory like LibriTTS, a structured directory was created where each video&#39;s audio and translated transcript are stored in a dedicated folder named after the video ID. This organization simplifies subsequent data processing steps.
4. Audio Segmentation: The next step was to process each video&#39;s audio file by segmenting it according to the transcript&#39;s timecodes. This step involved creating smaller audio files corresponding to specific transcript segments, facilitating more granular analysis and application.
5. Textual Content Cleaning: A cleaning procedure was implemented for the textual data to remove specific markers (e.g., &quot;[Ceol]&quot; indicating music) that may not be relevant for language learning applications. Files marked with these indicators were deleted to maintain the dataset&#39;s focus on spoken content.
6. Text Normalization: NLP techniques were applied to normalize the textual content. This process includes removing stopwords and punctuation, leveraging the spacy library and the stopwordsiso package for stopword removal in Irish. The goal is to refine the textual data for better NLP applications.


## To create a virtual environment run the following commands in the terminal:
```
pip3 install virtualenv
```
```
virtualenv {name_of_environment}
```
```
source name_of_environment/bin/activate
```

## To install all requirements, run this command in the terminal:
```
pip install -r requirements.txt
```
The code has a src folder, with the fucntions for the overall logic. There is a main file, which is the entry point to the code. I have also included a python notebook called CAMB_AI_Challenge which includes the entire workflow.

It can be run by using the command in the terminal:
```
python main.py
```

## Conclusion
This project represents a significant step towards creating valuable resources for the Irish language using modern technological tools. Through systematic extraction, processing, and normalization of YouTube content, a pipeline has been outlined that not only enriches Irish language resources but also showcases the potential for similar efforts in other less-resourced languages. The challenges encountered underscore the complexities of working with video and audio data, particularly in languages with limited digital footprints, and highlight the importance of innovative solutions in language preservation and education.
