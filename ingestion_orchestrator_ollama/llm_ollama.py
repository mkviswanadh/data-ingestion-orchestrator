# import subprocess

# def call_ollama(prompt: str, model: str = "phi") -> str:
#     try:
#         proc = subprocess.Popen(["ollama", "run", model],
#                                 stdin=subprocess.PIPE,
#                                 stdout=subprocess.PIPE,
#                                 stderr=subprocess.PIPE,
#                                 text=True)
#         stdout, stderr = proc.communicate(input=prompt)

#         if proc.returncode != 0:
#             raise Exception(f"Ollama failed: {stderr}")
#         return stdout
#     except Exception as e:
#         raise RuntimeError(f"Ollama invocation failed: {e}")

# llm_ollama.py
import requests

# llm_ollama.py

import requests

def call_ollama(prompt: str, model: str = "phi") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": True},
        stream=True,
        timeout=120,
    )
    
    response.raise_for_status()

    output = ""
    for line in response.iter_lines():
        if line:
            try:
                data = line.decode("utf-8")
                chunk = eval(data) if data.startswith("{") else {}
                output += chunk.get("response", "")
            except Exception as e:
                print(f"⚠️ Failed to parse line: {line}")
                continue

    return output.strip()


