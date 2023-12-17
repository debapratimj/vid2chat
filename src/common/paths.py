import os

# Base directories
# Compute the base directory
current_path = os.getcwd()
parts = current_path.split("vid2chat")
BASE_DIR = parts[0] + "/vid2chat"

SRC_DIR = os.path.join(BASE_DIR, 'src')
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

AUDIO_DIR = os.path.join(DATA_DIR, 'audio')
VIDEO_DIR = os.path.join(DATA_DIR, 'original_video')
SPLIT_VIDEO_DIR = os.path.join(DATA_DIR, 'segmented_video')
SPEAKER_0_DIR = os.path.join(SPLIT_VIDEO_DIR, 'speaker_0')
SPEAKER_1_DIR = os.path.join(SPLIT_VIDEO_DIR, 'speaker_1')
SRT_SPEAKER_0_DIR = os.path.join(OUTPUT_DIR, 'srt_speaker_0')
SRT_SPEAKER_1_DIR = os.path.join(OUTPUT_DIR, 'srt_speaker_1')
AUTH_DIR = os.path.join(DATA_DIR, 'auth')
OUTPUT_JSON_DIR = os.path.join(DATA_DIR, 'output_json')
