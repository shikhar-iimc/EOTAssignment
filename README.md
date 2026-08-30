# Ethics, Enabled and Constrained — Interactive Essay Supplement

An interactive companion to the essay *"Ethics, Enabled and Constrained: Reading Palantir, Google,
and Anthropic Through the Grammar of Military AI Narratives"*, written for *Ethics of Technology and
Its Relevance for Business* (IIM Calcutta, Term IV, AY 2026–27).

This is a **supplement**, not a substitute — the graded submission is the written essay. This site
exists to make the underlying research explorable: a theoretical framework, a sourced timeline, a
relationship map, full company profiles, the complete Palantir manifesto, and every citation used.

## What's inside

| Page | Content |
|---|---|
| `Home.py` | Landing page — thesis summary and navigation |
| `pages/1_Narrative_Framework.py` | Interactive quadrant chart of Malmio's four narratives, with each company plotted |
| `pages/2_Timeline.py` | Filterable, sourced timeline of every dated event across all three companies |
| `pages/3_Relationship_Map.py` | Node/edge map of who contracts with whom (Palantir, Google, Anthropic, DoD, and other clients) |
| `pages/4_Company_Profiles.py` | Deep-dive tabs per company — facts, key quotes, essay's analytical reading |
| `pages/5_The_Manifesto.py` | All 22 points of Palantir's "Technological Republic" thread, searchable/filterable |
| `pages/6_Sources.py` | Every citation used across the essay and this site, searchable |

## A note on honesty in the visuals

Every page consistently labels content as one of:
- **VERIFIED FACT** — a dated, sourced claim (news reporting, primary documents, court filings)
- **PRIMARY SOURCE** — direct quotation from an original document (e.g., the manifesto itself)
- **OUR INTERPRETATION** — the essay's own analytical argument about what the facts mean

The one chart that is *not* included here, deliberately, is a bar chart comparing the three
companies' "restrictiveness" on a numeric scale — an earlier draft of this idea implied a precision
that didn't exist (there is no dataset that measures this). The interactive quadrant in
`1_Narrative_Framework.py` replaces it with something more honest: a qualitative placement, clearly
labeled as interpretation, that you can hover over to see the specific reasoning rather than a number
that implies a measurement.

## Running locally

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Deploying on Streamlit Community Cloud

1. Push this folder to a GitHub repository (public or private, your choice).
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub.
3. Click "New app," select the repo, and set the main file path to `Home.py`.
4. Deploy. Streamlit Cloud will auto-detect `requirements.txt` and `.streamlit/config.toml`.

No secrets, API keys, or databases are used — this is a static-content app, so deployment should be
immediate with no configuration beyond the above.

## File structure

```
.
├── Home.py
├── data.py                  # single source of truth for all content/citations
├── styles.py                # shared CSS injected on every page
├── requirements.txt
├── .streamlit/
│   └── config.toml          # theme (matches the essay's color palette)
└── pages/
    ├── 1_Narrative_Framework.py
    ├── 2_Timeline.py
    ├── 3_Relationship_Map.py
    ├── 4_Company_Profiles.py
    ├── 5_The_Manifesto.py
    └── 6_Sources.py
```

To add or correct a fact, edit `data.py` only — every page reads from it, so there is a single place
to keep the content accurate and consistent.
