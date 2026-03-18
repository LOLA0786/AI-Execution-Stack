# AI Execution Stack

Run, control, and debug AI agents safely in production.

---

## 🔥 What This Is

A reference system that combines:

- BotBook → runs AI agents  
- PrivateVault → enforces policies before execution  
- LORK → provides replay, debugging, and observability  

---

## ⚡ Why This Exists

AI agents are starting to take real actions across tools and data.

But there is no control layer before execution.

This stack solves that.

---

## 🧪 Demo (2 min)

Run:

```bash
./start_demo.sh

This will:

Run an AI workflow

Enforce policy before execution

Log + enable replay

🎯 Pilot Use Case

Support AI response validation:

User → AI draft → policy check → approval → send → audit

🧠 Stack

BotBook → Execution layer
PrivateVault → Governance layer
LORK → Debugging layer

🚀 Goal

Validate this in a 2-week pilot on one workflow.

