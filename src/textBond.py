import json
import os
from common import paths
# read the output.json file and get the first value of the speaker key
# Specify the path to the output.json file
file_path = os.path.join(paths.OUTPUT_DIR, 'output.json')

time_threshold = 1.0

# Read the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

print(data[0]['speaker'])

# Get the first value of the speaker key
actual_speaker = data["speaker"][0]

conversation = {'speaker_0': [], 'speaker_1': []}

i = 0
while data[i]["speaker"] == actual_speaker:

    # Get the start and end time of the speaker
    start = data[i]["start"]
    end = data[i]["stop"]
    srt_file_path = f'{os.path.join(paths.SRT_SPEAKER_DIR, actual_speaker)}_{round(start, 3)}_{round(end, 3)}.srt'

    # Read the srt file
    with open(srt_file_path, "r") as srt_file:
        srt_text = srt_file.read()
    
    if actual_speaker[-1] == '0':
        conversation['speaker_0'].append([srt_text])
    else:
        conversation['speaker_1'].append([srt_text])

    i += 1
    actual_speaker = data[i]["speaker"]

# Write the conversation to a JSON file
with open(os.path.join(paths.OUTPUT_DIR, 'conversation.json'), 'w') as json_file:
    json.dump(conversation, json_file, indent=2)