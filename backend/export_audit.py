import json

def export_audit():
    with open("audit_chain.log") as f:
        data = [json.loads(x) for x in f.readlines()]
    return data
