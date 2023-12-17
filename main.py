import os
import subprocess
from audioHelper import *
from common import paths

def main():
    # speaker diarization
    subprocess.run(['python3', 'speaker.py'], cwd='src')

    # video splitting
    subprocess.run(['python3', 'split.py'], cwd='src')

    # srt generation for speaker 0
    for filename in os.listdir(paths.SPEAKER_0_DIR):
        subprocess.run(['auto_subtitle', 
                        '--model', 'large',
                        '--srt_only', 'true', 
                        '--task', 'translate', 
                        f'{os.path.join(paths.SPEAKER_0_DIR, filename)}', 
                        '-o', 
                        f'{os.path.join(paths.SRT_SPEAKER_0_DIR, filename[:-4])}.srt'])
        
    # srt generation for speaker 1
    for filename in os.listdir(paths.SPEAKER_1_DIR):
        subprocess.run(['auto_subtitle',
                        '--model', 'large', 
                        '--srt_only', 'true', 
                        '--task', 'translate', 
                        f'{os.path.join(paths.SPEAKER_1_DIR, filename)}', 
                        '-o', 
                        f'{os.path.join(paths.SRT_SPEAKER_1_DIR, filename[:-4])}.srt'])

if __name__ == '__main__':
    main()