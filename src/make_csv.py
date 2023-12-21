import os
import json
import pandas as pd
from common import paths

# Load data from the JSON file
with open(os.path.join(paths.OUTPUT_DIR, 'final_conversation.json')) as json_file:
    data = json.load(json_file)

# Create a Pandas DataFrame from the JSON data
df = pd.DataFrame.from_dict(data, orient='index')

# Transpose the DataFrame
df = df.transpose()

# Function to count the number of question marks in a sentence
def count_question_marks(sentence):
    return sentence.count('?')

# Apply the function to each cell in the DataFrame
question_marks_counts = df.apply(lambda x: x.map(lambda y: count_question_marks(str(y))))

# Sum the counts for each speaker
speaker_question_marks_counts = question_marks_counts.sum()

# Identify the speaker with more question marks
therapist = speaker_question_marks_counts.idxmax()
patient = speaker_question_marks_counts.idxmin()

# Reorganize the DataFrame based on the speaker with more question marks
if speaker_question_marks_counts[therapist] > speaker_question_marks_counts[patient]:
    df = df[[therapist, patient]]
else:
    df = df[[patient, therapist]]

# Rename the columns
df.columns = ['Therapist', 'Patient']

# write the dataframe to a csv file
df.to_csv(os.path.join(paths.OUTPUT_DIR, 'final_conversation.csv'), index=False)