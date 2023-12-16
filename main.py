import os
import argparse

from audioHelper import *
from common import paths
import subprocess

def main():
    # Load the audio file
    file_path = os.path.join(paths.AUDIO_DIR, 'audio_1.wav')
    file_path_out = os.path.join(paths.AUDIO_DIR, 'audio_1_resized.wav')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract conversation from video')
    parser.add_argument('--srt_only', type=bool, default=False, help='Generate SRT file only')
    parser.add_argument('--task', type=str, default='translate', help='Subtitle task')
    parser.add_argument('input_file', type=str, help='Input video file')
    parser.add_argument('-o', '--output_dir', type=str, default='subtitled/', help='Output directory')

    # scripts
    subprocess.run(['python3', 'speaker.py'], cwd='src')

    args = parser.parse_args()

    main()
    

if __name__ == '__main__':
    main()