from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_path, output_audio_path):
    """Extract audio from video"""
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)
