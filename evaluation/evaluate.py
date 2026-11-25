

import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

review = pd.read_csv(DATA / "human_review.csv", keep_default_na=False)
results = json.loads(
    (DATA / "research_results.json").read_text(encoding="utf-8")
)

fields = {
    "auth": ("agent_auth", "human_auth"),
    "access": ("agent_access", "human_access"),
    "verdict": ("agent_verdict", "human_verdict")
}

metrics = {}

for field, (agent_col, human_col) in fields.items():
    checked = review[
        (review[human_col].astype(str).str.strip() != "")
    ].copy()

    if checked.empty:
        metrics[field] = {
            "reviewed": 0,
            "first_pass_correct": None,
            "note": "No human labels supplied yet"
        }
        continue

    def normalize(value):
        if isinstance(value, list):
            return sorted(str(x).lower().strip() for x in value)
        return str(value).lower().strip()

    matches = [
        normalize(a) == normalize(h)
        for a, h in zip(checked[agent_col], checked[human_col])
    ]

    metrics[field] = {
        "reviewed": len(matches),
        "first_pass_correct": sum(matches),
        "first_pass_accuracy": round(
            sum(matches) / len(matches) * 100, 2
        ),
        "human_corrected_records": sum(not x for x in matches)
    }

summary = {
    "method": "Human-labeled stratified sample",
    "sample_size": len(review),
    "fields": metrics,
    "warning": (
        "Only rows with human labels are evaluated. "
        "This is not accuracy across all 100 apps. "
        "Human-reviewed corrections must be recorded separately."
    )
}

(DATA / "evaluation_summary.json").write_text(
    json.dumps(summary, indent=2),
    encoding="utf-8"
)

print(json.dumps(summary, indent=2))
