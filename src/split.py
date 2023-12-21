import json
import os
from helper import split_video
from common import paths

# Path to the original video file
VIDEO_PATH = os.path.join(paths.VIDEO_DIR, 'video.mp4')
# Path to the JSON file
OUTPUT_FILE = os.path.join(paths.OUTPUT_DIR, 'output.json')
# Path to the output video file
SPEAKER0_OUTPUT_VIDEO = paths.SPEAKER_0_DIR
SPEAKER1_OUTPUT_VIDEO = paths.SPEAKER_1_DIR

# Load the JSON file
with open(OUTPUT_FILE) as json_file:
    data = json.load(json_file)

# Split the video into desired parts
for i in range(len(data)):
    start = data[i]['start']
    end = data[i]['stop']
    speaker = data[i]['speaker']
    if speaker[-1] == '1':
        split_video(VIDEO_PATH, start, end, f'{os.path.join(SPEAKER1_OUTPUT_VIDEO, speaker)}_{round(start, 3)}_{round(end, 3)}.mp4')
    else:
        split_video(VIDEO_PATH, start, end, f'{os.path.join(SPEAKER0_OUTPUT_VIDEO, speaker)}_{round(start, 3)}_{round(end, 3)}.mp4')
        