import pyaudio
import numpy as np
import librosa

# Set up audio stream
audio_format = pyaudio.paFloat32
channels = 1
sample_rate = 44100
c_sec = 3
chunk_size = sample_rate*c_sec
stream = pyaudio.PyAudio().open(format=audio_format, channels=channels, rate=sample_rate,
                                 input=True, frames_per_buffer=chunk_size)

# Set up tempo and beat tracking parameters
hop_length = 512

# Process audio stream
while True:
    # Read audio data from stream
    data = stream.read(chunk_size)
    samples = librosa.util.buf_to_float(data, n_bytes=4, dtype=np.float32)

    # Compute tempo and beat times for current audio frame
    tempo, beat_times = librosa.beat.beat_track(y=samples, sr=sample_rate)

    # Print tempo and beat times
    print(f"Tempo: {tempo:.2f} BPM")
    print(f"Beat times (s): {beat_times}")
