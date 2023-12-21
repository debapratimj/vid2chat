import re
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

conversation = {'speaker_0': [], 'speaker_1': []}

# Define a regular expression pattern to match the text between the timestamps
pattern = r"\d+\n\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+\n(.+)"

# Loop through the data
for item in data:
    # Get the text from the current item
    text = item.get("text", "")
    # Use re.search to find the match
    match = re.search(pattern, text)

    # Determine the speaker and add the text to the conversation dictionary
    if item["speaker"].endswith('0'):
        conversation['speaker_0'].append(match.group(1))
    else:
        conversation['speaker_1'].append(match.group(1))


# Write the conversation to a JSON file
with open(os.path.join(paths.OUTPUT_DIR, 'conversation.json'), 'w') as json_file:
    json.dump(conversation, json_file, indent=2)
