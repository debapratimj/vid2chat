import librosa
import random
import soundfile


def cut_and_save_random_segment(input_file, output_file):
    try:
        # Load the audio file
        audio, sr = librosa.load(input_file, sr=None)

        # Set the desired duration (10 seconds)
        desired_duration = 40

        # Get the total duration of the audio
        total_duration = librosa.get_duration(y=audio, sr=sr)

        # Check if the audio is shorter than the desired duration
        if total_duration < desired_duration:
            raise ValueError("Audio duration is shorter than the desired duration.")

        # Randomly select a start time within the valid range
        start_time = random.uniform(0, total_duration - desired_duration)

        # Extract the 10-second segment
        start_sample = int(start_time * sr)
        end_sample = int((start_time + desired_duration) * sr)
        audio_segment = audio[start_sample:end_sample]

        # Save the segment as a new .wav file
        soundfile.write(output_file, audio_segment, sr)

        print(f"Successfully saved a 10-second segment to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


def save_text_to_file(text, output_file):
    with open(output_file, 'w') as file:
        file.write(text)
