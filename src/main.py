import librosa
import os

from audioHelper import *
#from videoHelper import *
from common import paths
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration

def main():
    # Load the audio file
    file_path = os.path.join(paths.AUDIO_DIR, 'audio_1.wav')
    file_path_out = os.path.join(paths.AUDIO_DIR, 'audio_1_resized.wav')
    cut_and_save_random_segment(file_path, file_path_out)

    model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-librispeech-asr")
    processor = Speech2TextProcessor.from_pretrained("facebook/s2t-small-librispeech-asr")

    # load audio
    waveform, sampling_rate = librosa.load(file_path_out, sr=None)
    # Resample the audio to 16000 Hz
    waveform_resampled = librosa.resample(waveform, orig_sr=sampling_rate, target_sr=16000)

    inputs = processor(waveform_resampled, sampling_rate=16000, return_tensors="pt")
    generated_ids = model.generate(inputs["input_features"], attention_mask=inputs["attention_mask"])

    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
    # TODO Write the text to a text file and save it
    print(transcription)

if __name__ == '__main__':
    main()