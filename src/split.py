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

# Split the video into desired parts
with open(OUTPUT_FILE) as json_file:
    data = json.load(json_file)
    for i in range(len(data)):
        start = data[i]['start']
        end = data[i]['stop']
        speaker = data[i]['speaker']
        if speaker[-1] == '1':
            split_video(VIDEO_PATH, start, end, f'{os.path.join(SPEAKER1_OUTPUT_VIDEO, speaker)}_{start:.2f}_{end:.2f}.mp4')
        else:
            split_video(VIDEO_PATH, start, end, f'{os.path.join(SPEAKER0_OUTPUT_VIDEO, speaker)}_{start:.2f}_{end:.2f}.mp4')
        