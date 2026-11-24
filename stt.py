from faster_whisper import WhisperModel
import numpy as np
import sounddevice as sd
import soundfile as sf


print("Loading model...")

model=WhisperModel("base", 
                   device="cpu", 
                   compute_type="int8")

print("Model loaded successfully.")

def transcribe(audio_file:str)-> str:
    segments, info = model.transcribe(audio_file)
    text = ""

    for segment in segments:
        text += segment.text    
    return text.strip()

def record_audio(filename:str):
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
                sf.write(filename, np.concatenate(audio), 16000)
                audio=[]
                break
        if not recording:
            continue