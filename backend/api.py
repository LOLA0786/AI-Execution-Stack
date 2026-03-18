from fastapi import FastAPI
import subprocess
import json

app = FastAPI()

@app.get("/run-demo")
def run_demo():
    result = subprocess.run(
        ["python3", "demo/real_demo.py"],
        capture_output=True,
        text=True
    )
    return {"output": result.stdout}
