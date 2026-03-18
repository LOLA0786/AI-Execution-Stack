from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/audit")
def get_audit():
    with open("audit_chain.log", "r") as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines]
