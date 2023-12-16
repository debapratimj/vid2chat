from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import json
from common import paths

def save_text_to_file(diarization, output_file):
    """Save the text to a file"""
    with open(output_file, "w") as f:
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            f.write(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}\n")
            # Save the result to a JSON file
            output_file = os.path.join(paths.OUTPUT_JSON_DIR, 'final_output.json')
            result = {}

            for turn, _, speaker in diarization.itertracks(yield_label=True):
                if speaker not in result:
                    result[speaker] = []
                result[speaker].append([turn.start, turn.end])

            with open(output_file, "w") as f:
                json.dump(result, f)

def extract_audio(video_path, output_audio_path):
    """Extract audio from video"""
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)
