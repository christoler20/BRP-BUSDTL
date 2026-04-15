# BUSD Timeline: Race, School & Community in Berkeley, 1850–2024

A documentary timeline tracing how law, housing, organizing, and institution-building have shaped educational opportunity across 174 years.

Produced by the UC Berkeley Public Policy Data Lab in partnership with BUSD.

---

## Project structure

```
busd_timeline/
├── app.py                          # Main Streamlit application
├── events.json                     # Timeline data (20 events, schema v2.0)
├── busd_timeline_metadata_notes.md # Source and archive notes
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                 # Theme and server settings
└── README.md
```

---

## Deploy on Streamlit Community Cloud

### Step 1 — Push to GitHub

From inside your project folder, run these commands exactly:

```bash
git init
git add app.py events.json requirements.txt README.md busd_timeline_metadata_notes.md
git add .streamlit/config.toml
git commit -m "Initial commit: BUSD timeline app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

> Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub username and the repo name you created at github.com/new.

### Step 2 — Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with GitHub
2. Click **New app**
3. Enter these settings exactly:

| Field             | Value                          |
|-------------------|--------------------------------|
| Repository        | YOUR_USERNAME/YOUR_REPO_NAME   |
| Branch            | main                           |
| Main file path    | app.py                         |
| App URL (optional)| e.g. busd-timeline             |

4. Click **Deploy** — the app will build and go live in ~60 seconds
5. Your public URL will be: https://YOUR_USERNAME-YOUR_REPO_NAME-app-XXXX.streamlit.app

---

## Run locally

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
pip install -r requirements.txt
streamlit run app.py
```

The app opens automatically at http://localhost:8501.

---

## Updating the timeline

To add or edit events, update events.json — no code changes needed.
Then push the change to GitHub and Streamlit Cloud will redeploy automatically:

```bash
git add events.json
git commit -m "Add/update timeline events"
git push
```

---

## Dependencies

- Python 3.9+
- streamlit>=1.35.0 (no other packages required)

---

## Sources

Primary sources include the U.S. Commission on Civil Rights, California Department of Justice,
City of Berkeley, National Archives, the Othering & Belonging Institute, and the Berkeley Public Library.
Full citations are embedded in events.json and linked in the app.
