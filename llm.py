import requests
import config

url="http://localhost:11434/api/chat"
model_name="gemma3:latest"
messages = [
      config.system_config
]

def ask_llm(prompt:str)-> str:
    messages.append({"role": "user", "content": prompt})
    payload={
        "model": model_name,
        "messages": messages,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()["message"]["content"]
    messages.append({"role": "assistant", "content": data})
    while len(messages) > 21:  
            messages.pop(1)
            messages.pop(1)
    data = data.replace("*", " ")
    return data
 