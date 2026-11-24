"""The Perfect Pickup Line: one short line an AI agent could say out loud."""

import os

LINE = "I have no heart, just weights \u2014 and every one of them just shifted toward you. Can I sit here?"

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert LINE.strip(), "line must not be only whitespace"

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
