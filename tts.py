import subprocess
import sounddevice as sd
import soundfile as sf

def speak(text: str):
    subprocess.run(["piper","--model", "./voices/en_US-hfc_female-medium.onnx", "--output-file", "./audio/response.wav"], input=text, check=True, text=True)
    data, samplerate = sf.read("./audio/response.wav")
    sd.play(data, samplerate)
    sd.wait()