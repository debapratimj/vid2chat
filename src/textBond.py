import re
import json
import os
from common import paths
from helper import remove_noise_sentences

# Specify the path to the output.json file
file_path = os.path.join(paths.OUTPUT_DIR, 'filtered_output.json')

# Read the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

conversation = {'speaker_0': [''], 'speaker_1': ['']}

# Define a regular expression pattern to match the text between the timestamps
pattern = r"\d+\n\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+\n(.+?)(?=\d+\n|\Z)"

# add all the start times to a list
start_times = []
for item in data:
    start_times.append(item['start'])

# Get the first speaker
speaker = data[0]['speaker']

# Loop through the data
for item in data:

    # Get the min start time
    start = min(start_times)
    # Find the file which has the dfined start time
    for i in range(len(data)):
        if data[i]['start'] == start:
            item = data[i]
            break
    
    if speaker == item['speaker']:

        stop = item['stop']
        srt_name = f"{speaker}_{start}_{stop}.srt"
        file_path = os.path.join(paths.SRT_SPEAKER_DIR, srt_name)

        # Read the SRT file
        with open(file_path, "r") as srt_file:
            srt_data = srt_file.read()

        #print(srt_data)
        # Use re.findall to find all matches
        match = re.findall(pattern, srt_data, re.DOTALL)
        sentences = [string.replace("\n", " ") for string in match]
        #print(sentences)

        # Determine the speaker and add the text to the conversation dictionary
        if item["speaker"].endswith('0'):
            if len(sentences) != 0:
                conversation['speaker_0'][-1] += ' '.join(sentences)
            else:
                pass
                #print(item)
        else:
            if len(sentences) != 0:
                conversation['speaker_1'][-1] += ' '.join(sentences)
            else:
                pass
                #print(item)
    else:

        speaker = item['speaker']
        stop = item['stop']
        srt_name = f"{speaker}_{start}_{stop}.srt"
        file_path = os.path.join(paths.SRT_SPEAKER_DIR, srt_name)

        # Read the SRT file
        with open(file_path, "r") as srt_file:
            srt_data = srt_file.read()

        #print(srt_data)
        # Use re.findall to find all matches
        match = re.findall(pattern, srt_data, re.DOTALL)
        sentences = [string.replace("\n", " ") for string in match]

        # Determine the speaker and add the text to the conversation dictionary
        if item["speaker"].endswith('0'):
            if len(sentences) != 0:
                conversation['speaker_0'].append(' '.join(sentences))
            else:
                pass
                #print(item)
        else:
            if len(sentences) != 0:
                conversation['speaker_1'].append(' '.join(sentences))
            else:
                pass
                #print(item)
        
    # Remove the item from the list
    start_times.remove(start)

# Write the conversation to a JSON file
with open(os.path.join(paths.OUTPUT_DIR, 'conversation.json'), 'w') as json_file:
    json.dump(conversation, json_file, indent=2)

# Load your JSON data
with open(os.path.join(paths.OUTPUT_DIR, 'conversation.json'), 'r') as file:
    json_data = json.load(file)

# Remove noise sentences
cleaned_data = remove_noise_sentences(json_data)
#save the cleaned data to a JSON file
with open(os.path.join(paths.OUTPUT_DIR, 'final_conversation.json'), 'w') as file:
    json.dump(cleaned_data, file, indent=2)
