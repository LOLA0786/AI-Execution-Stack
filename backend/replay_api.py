from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/replay")
def replay_last():
    with open("audit_chain.log", "r") as f:
        last = json.loads(f.readlines()[-1])
    return last
