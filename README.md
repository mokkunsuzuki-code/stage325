# Stage325: Verifiable Audit Report Export

Turn public verification infrastructure into a **submit-ready audit report package**.

Do not just export reports.  
Export verifiable proof packages.

---

## Overview

Stage324 made audit evidence publicly verifiable.

Stage325 upgrades it into an externally submit-ready audit report package in:

- JSON
- HTML
- PDF

The report is not just readable.  
It includes signed history, public verification files, and reproducible verification instructions.

---

## Core Idea

```text
audit history
  ↓
signed proof
  ↓
JSON / HTML / PDF report
  ↓
external submission
  ↓
third-party verification
Exported Report Files
docs/report/report.json
docs/report/report.html
docs/report/report.pdf
docs/report/verify.txt
Proof Files
docs/proofs/history.json
docs/proofs/history.json.sig
docs/proofs/public-key.asc
Verify
./verify_report.sh

Manual verification:

gpg --import docs/proofs/public-key.asc
gpg --verify docs/proofs/history.json.sig docs/proofs/history.json
What This Proves
The audit report exists.
The audit history has not been tampered with.
The report package includes verification instructions.
The exported report can be submitted externally.
Third parties can verify the proof using the public key and signature.
Stage Evolution
Stage324 = public verification
Stage325 = verifiable external audit submission
Live Demo

https://mokkunsuzuki-code.github.io/stage325/

Security Policy

Private keys, core logic, local secrets, and internal files must not be committed.

Excluded:

core/
keys/
*.pem
*.key
.env
.venv/
app.py
templates/
static/

Only public verification artifacts and report packages are published.

License

MIT License

Copyright (c) 2025 Motohiro Suzuki
