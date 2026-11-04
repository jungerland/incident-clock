# Breach Clock: an incident notification agent

You tell it a vendor was breached. It reads each customer contract, decides who is owed notice, calculates each deadline in code, and drafts each notice for counsel. It sends nothing.

**Demo and memo:** https://claude.ai/artifact/3q22aFqYC36LqojnzfnSYK

**Product memo:** [MEMO.md](MEMO.md)

All companies and contracts are fictional. Results are in `runs/`. See the memo's Caveats section for what they do and don't show.

## Run it

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

.venv/bin/python -m commitments.extract              # read the contracts, write the commitments
.venv/bin/python -m evals.score runs/<dir>           # score them
.venv/bin/python -m commitments.incident             # run the Labelforge incident
.venv/bin/python -m evals.score_incident runs/incidents/<dir> --flip runs/incidents/<flip dir>
.venv/bin/python -m ui.build                         # rebuild the page from recorded runs

.venv/bin/python -m evals.test_score                 # scorer and guardrail tests, no model calls
.venv/bin/python -m evals.test_incident
```

The flip run uses the limited data set log:

```
.venv/bin/python -m commitments.incident --label flip --only EHS \
  --transfer-log fixtures/exampleco/incident-labelforge/labelforge-transfer-log-limited-data-set.csv
```

Model calls need Anthropic credentials, from `ant auth login` or `ANTHROPIC_API_KEY`.
