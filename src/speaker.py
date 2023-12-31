import json
import os
import torch
from pyannote.audio import Pipeline
from helper import extract_audio
from common import paths
import os

AUTH_TOKEN = "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"
AUDIO_PATH = os.path.join(paths.AUDIO_DIR, 'audio.wav')
VIDEO_PATH = os.path.join(paths.VIDEO_DIR, 'video.mp4')
OUTPUT_FILE = os.path.join(paths.OUTPUT_DIR, 'output.json')
FINAL_OUTPUT_FILE = os.path.join(paths.OUTPUT_DIR, 'final_output.json')

pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=AUTH_TOKEN)

# Extract the audio from the video
extract_audio(VIDEO_PATH, AUDIO_PATH)

# send pipeline to GPU (when available)
pipeline.to(torch.device("cuda"))

# apply pretrained pipeline
diarization = pipeline(AUDIO_PATH)

# Create a list to store the information
diarization_info = []

# Assuming your existing code for diarization
for turn, _, speaker in diarization.itertracks(yield_label=True):
    entry = {
        "start": round(turn.start, 3),
        "stop": round(turn.end, 3),
        "speaker": speaker
    }
    diarization_info.append(entry)

# Convert the last stop time to int to avoid diarization error for the last video segment
diarization_info[-1]['stop'] = int(diarization_info[-1]['stop'])

# Write the information to the JSON file
with open(OUTPUT_FILE, 'w') as json_file:
    json.dump(diarization_info, json_file, indent=2)
    # close the file
    json_file.close()

print(f"\nDiarization information has been written to {OUTPUT_FILE}")
