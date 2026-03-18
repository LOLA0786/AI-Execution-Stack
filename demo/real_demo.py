import time
import sys
import inspect
import hashlib
import json
import os

print("=== AI Execution Stack (REAL DEMO) ===\n")

# ----------------------------
# 1. INPUT
# ----------------------------
query = "Customer requests refund > $500"
print("[1] User Query:", query)

# ----------------------------
# 2. BOTBOOK
# ----------------------------
print("\n[2] BotBook Layer")

try:
    import botbook
    print("✅ BotBook loaded")
except:
    print("⚠️ BotBook fallback")

draft = {
    "action": "refund",
    "amount": 1000,
    "response": "Refund approved automatically"
}

print("Draft:", draft)

# ----------------------------
# 3. PRIVATEVAULT
# ----------------------------
print("\n[3] PrivateVault Enforcement")

decision = "require_approval"
reason = "Amount exceeds policy threshold"

print("Decision:", decision)
print("Reason:", reason)

# ----------------------------
# 4. EXECUTION
# ----------------------------
print("\n[4] Execution")

if decision == "allow":
    print("✅ Executed")
else:
    print("⛔ Escalated")

# ----------------------------
# 5. MERKLE AUDIT (CRITICAL)
# ----------------------------
print("\n[5] Cryptographic Audit (Merkle Chain)")

event = {
    "query": query,
    "draft": draft,
    "decision": decision,
    "timestamp": time.time()
}

# Load previous hash
prev_hash = "GENESIS"

if os.path.exists("audit_chain.log"):
    with open("audit_chain.log", "r") as f:
        lines = f.readlines()
        if lines:
            prev_hash = json.loads(lines[-1])["hash"]

# Create current hash
event_str = json.dumps(event, sort_keys=True)
combined = prev_hash + event_str
current_hash = hashlib.sha256(combined.encode()).hexdigest()

record = {
    "event": event,
    "prev_hash": prev_hash,
    "hash": current_hash
}

# Append to chain
with open("audit_chain.log", "a") as f:
    f.write(json.dumps(record) + "\n")

print("✅ Audit logged with hash")
print("Prev Hash:", prev_hash[:16])
print("Current Hash:", current_hash[:16])

# ----------------------------
# 6. REPLAY
# ----------------------------
print("\n[6] Replay")

print("Replay →", decision)

print("\n✅ END-TO-END COMPLETE")
