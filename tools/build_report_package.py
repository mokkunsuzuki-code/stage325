#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(".")
REPORT_DIR = ROOT / "docs" / "report"
PUBLIC_REPORT_DIR = ROOT / "public" / "report"

REPORT_DIR.mkdir(parents=True, exist_ok=True)
PUBLIC_REPORT_DIR.mkdir(parents=True, exist_ok=True)

report = {
    "stage": 325,
    "title": "Verifiable Audit Report Export",
    "issuer": "Motohiro Suzuki",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "formats": ["JSON", "HTML", "PDF"],
    "status": "submission_ready",
    "summary": "This package exports a verifiable audit report in JSON, HTML, and PDF formats.",
    "verification": {
        "history": "proofs/history.json",
        "signature": "proofs/history.json.sig",
        "public_key": "proofs/public-key.asc",
        "command": "gpg --import proofs/public-key.asc && gpg --verify proofs/history.json.sig proofs/history.json"
    },
    "what_this_proves": [
        "The audit report exists.",
        "The audit history has not been tampered with.",
        "The report includes reproducible verification instructions.",
        "The package is ready for external submission."
    ],
    "stage_evolution": {
        "stage324": "Multi-signature-ready public verification",
        "stage325": "Verifiable audit report export package"
    }
}

json_path = REPORT_DIR / "report.json"
html_path = REPORT_DIR / "report.html"
pdf_path = REPORT_DIR / "report.pdf"
verify_path = REPORT_DIR / "verify.txt"

json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Stage325 Audit Report</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 900px; margin: 40px auto; line-height: 1.6; }}
.box {{ border: 1px solid #ddd; border-radius: 12px; padding: 20px; margin: 20px 0; }}
pre {{ background: #f6f6f6; padding: 12px; border-radius: 8px; overflow-x: auto; }}
</style>
</head>
<body>
<h1>Stage325: Verifiable Audit Report Export</h1>
<p><b>Submit the report. Let others verify the proof.</b></p>

<div class="box">
<h2>Summary</h2>
<p>{report["summary"]}</p>
</div>

<div class="box">
<h2>Verification Command</h2>
<pre>{report["verification"]["command"]}</pre>
</div>

<div class="box">
<h2>Proof Files</h2>
<ul>
<li><a href="../proofs/history.json">history.json</a></li>
<li><a href="../proofs/history.json.sig">history.json.sig</a></li>
<li><a href="../proofs/public-key.asc">public-key.asc</a></li>
</ul>
</div>

<div class="box">
<h2>What This Proves</h2>
<ul>
<li>The audit report exists.</li>
<li>The audit history has not been tampered with.</li>
<li>The report includes reproducible verification instructions.</li>
<li>The package is ready for external submission.</li>
</ul>
</div>
</body>
</html>
"""
html_path.write_text(html, encoding="utf-8")

verify_txt = """Stage325 Verification

Import public key:
gpg --import proofs/public-key.asc

Verify signed history:
gpg --verify proofs/history.json.sig proofs/history.json

If verification succeeds, the audit history has not been changed since signing.
"""
verify_path.write_text(verify_txt, encoding="utf-8")

# Minimal valid PDF using standard library only.
pdf_text = """Stage325: Verifiable Audit Report Export

Submit the report. Let others verify the proof.

Verification:
gpg --import proofs/public-key.asc
gpg --verify proofs/history.json.sig proofs/history.json

Proof files:
- proofs/history.json
- proofs/history.json.sig
- proofs/public-key.asc

This PDF is part of a verifiable audit report package.
"""

def escape_pdf(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

lines = pdf_text.splitlines()
content = "BT /F1 12 Tf 50 780 Td "
for i, line in enumerate(lines):
    if i:
        content += "0 -18 Td "
    content += f"({escape_pdf(line)}) Tj "
content += "ET"

objects = []
objects.append("1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj")
objects.append("2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj")
objects.append("3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >> endobj")
objects.append("4 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj")
objects.append(f"5 0 obj << /Length {len(content.encode('latin-1'))} >> stream\n{content}\nendstream endobj")

pdf = "%PDF-1.4\n"
offsets = [0]
for obj in objects:
    offsets.append(len(pdf.encode("latin-1")))
    pdf += obj + "\n"
xref_pos = len(pdf.encode("latin-1"))
pdf += f"xref\n0 {len(objects)+1}\n"
pdf += "0000000000 65535 f \n"
for off in offsets[1:]:
    pdf += f"{off:010d} 00000 n \n"
pdf += f"trailer << /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n"

pdf_path.write_bytes(pdf.encode("latin-1"))

for path in [json_path, html_path, pdf_path, verify_path]:
    target = PUBLIC_REPORT_DIR / path.name
    target.write_bytes(path.read_bytes())

print("[OK] wrote docs/report/report.json")
print("[OK] wrote docs/report/report.html")
print("[OK] wrote docs/report/report.pdf")
print("[OK] wrote docs/report/verify.txt")
