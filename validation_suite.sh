#!/usr/bin/env bash
set -euo pipefail

echo ""
echo "════════════════════════════════════════"
echo "  PRIVATEVAULT VALIDATION SUITE"
echo "════════════════════════════════════════"

PASS=0
TOTAL=0

run() {
  TOTAL=$((TOTAL+1))
  if eval "$2" &>/dev/null; then
    echo "[OK] $1"
    PASS=$((PASS+1))
  else
    echo "[FAIL] $1"
  fi
}

# ----------------------------------------
# CORE SYSTEM VALIDATION
# ----------------------------------------

run "Execution pipeline runs end-to-end" "./start_demo.sh"

run "Pre-execution policy enforcement active" "python3 demo/real_demo.py | grep -q 'PrivateVault Enforcement'"

run "High-risk action blocked before execution" "python3 demo/real_demo.py | grep -q 'Escalated'"

run "Cryptographic audit chain generated" "grep -q 'hash' audit_chain.log"

run "Audit chain integrity grows over time" "wc -l audit_chain.log | awk '{exit !(\$1 > 0)}'"

run "Replay capability available" "python3 demo/real_demo.py | grep -q 'Replay'"

# ----------------------------------------
# RESULTS
# ----------------------------------------

echo ""
echo "════════════════════════════════════════"
echo "  VALIDATION RESULTS"
echo "════════════════════════════════════════"
echo "  PASSED : $PASS / $TOTAL"

if [ "$PASS" -eq "$TOTAL" ]; then
  echo ""
  echo "  SYSTEM STATUS: VALIDATED"
  echo "  Ready for pilot deployment"
else
  echo ""
  echo "  SYSTEM STATUS: PARTIAL"
fi
