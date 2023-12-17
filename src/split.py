import json
import os
from helper import split_video
from common import paths

# Path to the original video file
VIDEO_PATH = os.path.join(paths.VIDEO_DIR, 'video.mp4')
# Path to the JSON file
OUTPUT_FILE = os.path.join(paths.OUTPUT_DIR, 'output.json')
# Path to the output video file
OUTPUT_VIDEO = paths.SPLIT_VIDEO_DIR

# Split the video into desired parts
with open(OUTPUT_FILE) as json_file:
    data = json.load(json_file)
    for i in range(len(data)):
        start = data[i]['start']
        end = data[i]['end']
        speaker = data[i]['speaker']
        split_video(VIDEO_PATH, start, end, f'{os.path.join(OUTPUT_VIDEO, speaker)}_{start}_{end}.mp4')