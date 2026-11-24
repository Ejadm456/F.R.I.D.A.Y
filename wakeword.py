from faster_whisper import WhisperModel
import sounddevice as sd
import soundfile as sf
from tts import speak

model=WhisperModel("tiny", 
                   device="cpu", 
                   compute_type="int8")

def record_wake_audio(filename: str):
    duration = 2
    sample_rate = 16000

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(filename, recording, sample_rate)

def transcribe_audio(filename: str) -> str:
    segments, info = model.transcribe(filename)
    text = ""
    for segment in segments:
        text += segment.text
    return text.strip()

def is_wake_word(text: str) -> bool:
    return "friday" in text.lower()

def wait_for_wake_word():
    while True:
        record_wake_audio("audio/wake.wav")
        text = transcribe_audio("audio/wake.wav")

        if is_wake_word(text):
            speak("Hello,how can i help you today?")
            return True