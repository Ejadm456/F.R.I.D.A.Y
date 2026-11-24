from llm import ask_llm
from wakeword import wait_for_wake_word
from stt import record_audio, transcribe
from tts import speak
from tools.router import handle_tool

def main():
    print("="*40)
    print("F.R.I.D.A.Y-Your AI Voice Assistant")
    print("="*40)

    while True:
        print("Listening for wake word...")
        wait_for_wake_word()
        while True:
            record_audio("audio/temp.wav")
            question = transcribe("audio/temp.wav")
            if "bye" in question.lower() or question.strip() == "":
                print("Goodbye!")
                speak("See you later.")
                break
            response = ask_llm(question) 
            tool_result = handle_tool(response)
            if tool_result:
                print(f"F.R.I.D.A.Y: {tool_result}")
                speak(tool_result)
            else:
                print(f"F.R.I.D.A.Y: {response}")
                speak(response)

if __name__ == "__main__":
    main()
