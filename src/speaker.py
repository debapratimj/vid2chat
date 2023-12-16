import json
import os
import torch
from pyannote.audio import Pipeline
from helper import extract_audio
from common import paths

# Get the authentication token from the JSON data
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
with open(OUTPUT_FILE, "w") as f:
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        f.write(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}\n")
        # Save the result to a JSON file
        result = {}

        for turn, _, speaker in diarization.itertracks(yield_label=True):
            if speaker not in result:
                result[speaker] = []
            result[speaker].append([turn.start, turn.end])

        with open(FINAL_OUTPUT_FILE, "w") as f:
            json.dump(result, f)




# start=0.2s stop=1.5s speaker_0
# start=1.8s stop=3.9s speaker_1
# start=4.2s stop=5.7s speaker_0
# ...