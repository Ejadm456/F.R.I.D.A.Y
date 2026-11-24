import sounddevice as sd

treshold=0.004
recording = False
silence=0
audio=[]

print("Ask something...")

stream = sd.InputStream(samplerate=16000, channels=1, dtype="float32")
stream.start()

while True:
    data, overflow = stream.read(1600)
    volume = 0
    for i in data:
        volume += abs(i[0])
    volume /= len(data)
    if volume > treshold:
        recording = True
    if recording:
        audio.append(data)
        if volume> treshold:
            silence = 0
        elif volume < treshold:
            silence += 1
        if silence >= 10:
            print("Recording stopped due to silence.")
            break
    if not recording:
        continue