#!/bin/bash
set -e

echo "Importing public key..."
gpg --import docs/proofs/public-key.asc

echo "Verifying signed audit history..."
gpg --verify docs/proofs/history.json.sig docs/proofs/history.json

echo "Checking report package..."
test -f docs/report/report.json
test -f docs/report/report.html
test -f docs/report/report.pdf
test -f docs/report/verify.txt

echo "OK: Stage325 report package is present and verifiable."
