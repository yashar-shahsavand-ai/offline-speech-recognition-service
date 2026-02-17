from faster_whisper import WhisperModel
import numpy as np

model = WhisperModel("medium", compute_type="int8")

def transcribe(audio_chunk):
audio = np.squeeze(audio_chunk)

```
segments, _ = model.transcribe(
    audio,
    language=None,
    vad_filter=True,
    beam_size=1
)

text = ""
for segment in segments:
    text += segment.text

return text.strip()
```
