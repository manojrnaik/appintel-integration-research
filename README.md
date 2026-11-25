# appintel-integration-research
AppIntel — AI Integration Research Agent

AppIntel is an evidence-led research pipeline that investigates 100 SaaS applications and evaluates their readiness for AI-agent integrations.

What it does
Discovers public developer documentation.
Extracts authentication and credential-access requirements.
Classifies API surface and MCP availability.
Evaluates integration buildability and blockers.
Audits extracted claims against collected evidence.
Generates JSON, CSV, and HTML outputs.
Creates a stratified human-review sample.
Architecture

DDGS search → Python evidence collection → Gemini structured extraction → evidence audit → human verification → dashboard.

Requirements
Python 3.11+
Gemini API key
Internet access
Setup
bash
git clone YOUR_REPOSITORY_URL
cd appintel-integration-research

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt


Create .env:

env
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-3.8-flash

Run

Test five applications:

bash
python agent/researcher.py --limit 5


Run the complete research set:

bash
python agent/researcher.py --limit 100

Evaluate

Manually review data/human_review.csv, then run:

bash
python evaluation/evaluate.py

Outputs
data/research_results.json
data/research_results.csv
data/human_review.csv
data/evaluation_summary.json
dashboard/index.html
Limitations

Public documentation does not establish that credentials can actually be issued without account approval. An MCP server not found in search is not proof of non-existence. Authenticated API testing and partner-gated access require additional human investigation.

All accuracy claims must be based on completed human review, not model confidence.

Reproducibility

The research dataset preserves source URLs, evidence extracts, timestamps, first-pass classifications, and audit findings. API keys must never be committed to the repository.

Project

Built as an AI Product Operations take-home case study for Composio.
