import os

# Base directories
# Compute the base directory
current_path = os.getcwd()
parts = current_path.split("vid2chat")
BASE_DIR = parts[0] + "/vid2chat"

DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

AUDIO_DIR = os.path.join(DATA_DIR, 'audio')
VIDEO_DIR = os.path.join(DATA_DIR, 'video')
AUTH_DIR = os.path.join(DATA_DIR, 'auth')
OUTPUT_JSON_DIR = os.path.join(DATA_DIR, 'output_json')
