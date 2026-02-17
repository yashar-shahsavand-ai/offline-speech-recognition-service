import sounddevice as sd
import queue
import numpy as np

SAMPLE_RATE = 16000
CHANNELS = 1

audio_queue = queue.Queue()

def callback(indata, frames, time, status):
if status:
print(status)
audio_queue.put(indata.copy())

def start_recording():
stream = sd.InputStream(
samplerate=SAMPLE_RATE,
channels=CHANNELS,
callback=callback,
blocksize=8000
)
stream.start()
return stream
