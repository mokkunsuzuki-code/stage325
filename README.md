# Stage324: Multi-Signed Public Verification Page

Turn audit history into a **multi-signature-ready public verification proof**.

Do not just trust logs.  
Verify who approved them.

---

## Overview

Stage323 added YubiKey/GPG issuer assurance to audit history.

Stage324 upgrades it into a **multi-signature-ready public verification page**.

The goal is simple:

> Move from individual accountability to organization-level approval.

---

## Core Idea

```text
history.json
  ↓
signature 1
  ↓
signature 2
  ↓
public keys
  ↓
third-party verification
  ↓
public browser verification page
What Stage324 Adds
Multi-signature-ready folder structure
Detached GPG signature files
Public key export
Public verification page
Terminal verification script
Browser-visible verification instructions
Files
docs/proofs/history.json
docs/proofs/history.json.sig
docs/proofs/public-key.asc
docs/proofs/signatures/history.motohiro.asc
verify_signature.sh
verify_multisig.sh
Verify
./verify_signature.sh

Or:

./verify_multisig.sh

Manual verification:

gpg --import docs/proofs/public-key.asc
gpg --verify docs/proofs/signatures/history.motohiro.asc docs/proofs/history.json
What This Proves
The audit history exists.
The audit history has not been tampered with.
The audit history is signed by an identifiable issuer.
The verification process is public and reproducible.
The structure is ready for multiple signatures.
Stage Evolution
Stage322 = audit infrastructure
Stage323 = issuer-backed audit infrastructure
Stage324 = multi-signature-ready public verification infrastructure
Who Needs This?
Security teams
Compliance teams
AI report verification workflows
Organizations requiring approval evidence
Anyone needing externally verifiable audit accountability
Live Demo

https://mokkunsuzuki-code.github.io/stage324/

Security Policy

Private keys, core logic, local secrets, and internal files must not be committed.

Excluded:

core/
keys/
*.pem
*.key
*.p12
.env
.env.*
.venv/

Only public verification artifacts are published.

License

MIT License

Copyright (c) 2025 Motohiro Suzuki
