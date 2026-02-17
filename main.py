import time
from recorder import start_recording, audio_queue
from transcriber import transcribe
from rich import print

def main():
print("[green]Realtime Local Speech Recognition Started...[/green]")
stream = start_recording()

```
buffer = []

try:
    while True:
        if not audio_queue.empty():
            chunk = audio_queue.get()
            buffer.append(chunk)

        if len(buffer) >= 5:
            import numpy as np
            audio_data = np.concatenate(buffer, axis=0)
            buffer = []

            text = transcribe(audio_data)

            if text:
                print(f"[cyan]You:[/cyan] {text}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping...")
    stream.stop()
```

if **name** == "**main**":
main()
