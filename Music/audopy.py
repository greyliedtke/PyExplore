import librosa
import numpy as np
import pyaudio
import time

# Parameters for audio stream
chunk_size = 1024
sample_rate = 44100

# Initialize PyAudio stream
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size, input_device_index=9)

def get_audio_dev():
    # Get the number of available input devices
    num_devices = audio.get_device_count()

    # Print the name and index of each input device
    for i in range(num_devices):
        device_info = audio.get_device_info_by_index(i)
        print("Device index:", i)
        print("Device name:", device_info["name"])

def get_amp():
    data = stream.read(chunk_size, exception_on_overflow=False)
        
    # Convert audio data to numpy array
    y = np.frombuffer(data, dtype=np.float32)
    
    # Compute amplitude
    amplitude = np.abs(librosa.stft(y))
    
    # Compute average amplitude
    avg_amplitude = np.mean(amplitude)

    return avg_amplitude



# Loop to capture and process audio in real-time
def tempo_amp():
    while True:
        # Read audio data from stream
        data = stream.read(chunk_size, exception_on_overflow=False)
        
        # Convert audio data to numpy array
        y = np.frombuffer(data, dtype=np.float32)
        
        # Compute tempo and beats
        tempo, beats = librosa.beat.beat_track(y=y, sr=sample_rate)
        
        # Compute amplitude
        amplitude = np.abs(librosa.stft(y))
        
        # Compute average amplitude
        avg_amplitude = np.mean(amplitude)
        
        # Print tempo and amplitude values
        print(f'Tempo: {tempo:.2f} BPM')
        print(f'Amplitude: {avg_amplitude:.2f}')
        # time.sleep(.5)