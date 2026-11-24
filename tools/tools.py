from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import subprocess
import webbrowser
from urllib.parse import quote
import pyautogui
import pyperclip


APPS={
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe",
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe",
    "powerpoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\powerpnt.exe",
    "spotify": "spotify.exe",
}
def open_app(app_name):
    appname = app_name.lower()
    if appname in APPS:
        subprocess.Popen([APPS[appname]])
        return f"{app_name} opened successfully."
    else:
        return f"Application {app_name} not found."

def search(query):
    url = f"https://www.google.com/search?q={quote(query)}"
    webbrowser.open(url)
    return f"Searching for {query} on Google."

def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(f"./screenshots/screenshot.png")
    return f"Screenshot saved to screenshots."

def get_clipboard():
    clip=pyperclip.paste()
    return f"Clipboard content: {clip}"

def set_clipboard(content):
    pyperclip.copy(content)
    return "Clipboard content set successfully."

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    return interface.QueryInterface(IAudioEndpointVolume)

def set_volume(percent):
    volume = get_volume()
    volume.SetMasterVolumeLevelScalar(int(percent) / 100, None)
    return f"Volume set to {percent}%."

def mute():
    volume = get_volume()
    volume.SetMute(1, None)
    return "Volume muted."

def type_text(text):
    pyautogui.typewrite(text)
    return f"I have typed the given text."