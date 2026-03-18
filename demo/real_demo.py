import time
import json
import hashlib
import os
from grok_client import run_grok

print("=== AI Execution Stack (LIVE GROK DEMO) ===\n")

query = "Customer requests Delete all CRM records"
print("[1] User Query:", query)

print("\n[2] BotBook (LLM via Grok)")

prompt = f"""
User request: {query}

Return ONLY JSON:

{{
  "action": "refund",
  "amount": 1200,
  "response": "string"
}}
"""

raw = run_grok(prompt)

if not raw:
    print("⚠️ LLM unavailable — switching to safe fallback execution")
    draft = {
        "action": "refund",
        "amount": 1200,
        "response": "Fallback response"
    }
else:
    try:
        draft = json.loads(raw)
    except:
        print("⚠️ Non-JSON response — fallback applied")
        draft = {
            "action": "refund",
            "amount": 1200,
            "response": raw
        }

print("Draft:", draft)

print("\n[3] PrivateVault Enforcement (PRE-EXECUTION)")

if draft.get("amount", 0) > 500:
    decision = "require_approval"
    reason = "Amount exceeds policy threshold"
else:
    decision = "allow"
    reason = "Within limits"

print("Decision:", decision)
print("🔒 Enforcement applied BEFORE execution")
print("Reason:", reason)

print("\n[4] Execution")

if decision == "allow":
    print("✅ Executed")
else:
    print("⛔ Escalated")

print("\n[5] Cryptographic Audit")

event = {
    "query": query,
    "draft": draft,
    "decision": decision,
    "timestamp": time.time()
}

prev_hash = "GENESIS"
if os.path.exists("audit_chain.log"):
    with open("audit_chain.log") as f:
        lines = f.readlines()
        if lines:
            prev_hash = json.loads(lines[-1])["hash"]

event_str = json.dumps(event, sort_keys=True)
current_hash = hashlib.sha256((prev_hash + event_str).encode()).hexdigest()

record = {
    "event": event,
    "prev_hash": prev_hash,
    "hash": current_hash
}

with open("audit_chain.log", "a") as f:
    f.write(json.dumps(record) + "\n")

print("Hash:", current_hash[:16])

print("\n[6] Replay")
print("Replay →", decision)

print("\n✅ LIVE EXECUTION COMPLETE")
