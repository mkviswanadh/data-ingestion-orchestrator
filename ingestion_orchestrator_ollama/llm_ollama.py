import subprocess

def call_ollama(prompt: str, model: str = "codellama") -> str:
    try:
        proc = subprocess.Popen(["ollama", "run", model],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        stdout, stderr = proc.communicate(input=prompt)

        if proc.returncode != 0:
            raise Exception(f"Ollama failed: {stderr}")
        return stdout
    except Exception as e:
        raise RuntimeError(f"Ollama invocation failed: {e}")

