import json
import os
from common import paths

# Specify the path to the output.json file
file_path = os.path.join(paths.OUTPUT_DIR, 'output.json')

time_threshold = 1.0

# Read the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

# go through data and remove the elements with less than 2 seconds
filtered_data = []
for i in range(len(data)):
  if (float(data[i]['stop']) - float(data[i]['start'])) >= time_threshold:
    filtered_data.append(data[i])

# write the filtered data to a json file
with open(os.path.join(paths.OUTPUT_DIR, 'filtered_output.json'), 'w') as outfile:
    json.dump(filtered_data, outfile)