#from moviepy.video.io.VideoFileClip import VideoFileClip
import json
from common.noise_words import noise_words
'''
def extract_audio(video_path, output_audio_path):
    """Extract audio from video"""
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)

def split_video(input_path, start_time, end_time, output_path="output.mp4"):
    """
    Split a video and save the specified portion to a new file.

    Parameters:
    - input_path (str): Path to the input video file.
    - start_time (float): Start time in seconds.
    - end_time (float): End time in seconds.
    - output_path (str): Path for the output video file (default is "output.mp4").
    """
    try:
        # Load the video clip
        video_clip = VideoFileClip(input_path)

        # Set the start and end times for the subclip
        subclip = video_clip.subclip(start_time, end_time)

        # Write the subclip to the output file
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        print(f"Video successfully split and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")
'''
# Function to check if a sentence is noise
def is_noise(sentence, noise_list=noise_words):
    return all(word.lower() in noise_list for word in sentence.split())

def remove_noise_sentences(json_data):
    # Process the JSON data
    processed_data = {}
    for speaker, sentences in json_data.items():
        processed_sentences = [sentence for sentence in sentences if not is_noise(sentence)]
        processed_data[speaker] = processed_sentences

    return processed_data