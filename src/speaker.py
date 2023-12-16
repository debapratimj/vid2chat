import json
import os
import torch
from pyannote.audio import Pipeline
from helper import extract_audio
from common import paths
import os

AUTH_TOKEN = "Replace this with your authentication token"
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

# Save the result to a file

if not os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "w") as f:
        f.write("{}")

with open(OUTPUT_FILE, "r+") as f:
    result = json.load(f)
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        if speaker not in result:
            result[speaker] = []
        result[speaker].append([turn.start, turn.end])

    with open(FINAL_OUTPUT_FILE, "w") as f:
        json.dump(result, f)
