import re
import json
import os
from common import paths

# Specify the path to the output.json file
file_path = os.path.join(paths.OUTPUT_DIR, 'output.json')

time_threshold = 1.0

# Read the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

conversation = {'speaker_0': [], 'speaker_1': []}

# Define a regular expression pattern to match the text between the timestamps
pattern = r"\d+\n\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+\n(.+)"

# add all the start times to a list
start_times = []
for item in data:
    start_times.append(item['start'])

# Loop through the data
for item in data:

    # Get the min start time
    start = min(start_times)
    # Find the file which has the dfined start time
    for i in range(len(data)):
        if data[i]['start'] == start:
            item = data[i]
            break
    
    speaker = item['speaker']
    stop = item['stop']
    srt_name = f"{speaker}_{start}_{stop}.srt"
    file_path = os.path.join(paths.SRT_SPEAKER_DIR, srt_name)

    # Read the SRT file
    with open(file_path, "r") as srt_file:
        srt_data = srt_file.read()

    print(srt_data)
    # Use re.search to find the match
    match = re.search(pattern, srt_data)

    # Determine the speaker and add the text to the conversation dictionary
    if item["speaker"].endswith('0'):
        try:
            conversation['speaker_0'].append(match.group(1))
        except:
            pass
            #raise('Sequence issue, The data might contain irrelevant information')
    else:
        try:
            conversation['speaker_1'].append(match.group(1))
        except:
            pass    
            #raise('Sequence issue, The data might contain irrelevant information')
        
    # Remove the item from the list
    start_times.remove(start)

# Write the conversation to a JSON file
with open(os.path.join(paths.OUTPUT_DIR, 'conversation.json'), 'w') as json_file:
    json.dump(conversation, json_file, indent=2)
