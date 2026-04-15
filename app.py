import json
import streamlit as st
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
# Resolve relative to this file so it works both locally and on Streamlit Cloud
BASE_DIR  = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "events.json"

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BUSD Timeline: Race, School & Community",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_events():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["events"]

events = load_events()

# ── Category config ───────────────────────────────────────────────────────────
CATEGORY_CONFIG = {
    "California": {
        "color": "#8B3A2A",
        "bg":    "#FDF0EC",
        "border":"#C4614A",
        "label": "California",
        "icon":  "⚖️",
    },
    "Berkeley": {
        "color": "#1F4E6B",
        "bg":    "#EBF4FA",
        "border":"#3A7EA8",
        "label": "Berkeley",
        "icon":  "🏘️",
    },
    "BUSD": {
        "color": "#2A5C3F",
        "bg":    "#EBF6EF",
        "border":"#4A9B68",
        "label": "BUSD",
        "icon":  "🏫",
    },
    "National": {
        "color": "#5C4200",
        "bg":    "#FDF6E3",
        "border":"#C4960A",
        "label": "National",
        "icon":  "🏛️",
    },
}

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Source Serif 4', Georgia, serif;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 960px;
}

/* ── Masthead ── */
.masthead {
    border-top: 4px solid #1a1a1a;
    border-bottom: 1px solid #1a1a1a;
    padding: 2.2rem 0 1.6rem 0;
    margin-bottom: 0.5rem;
    text-align: left;
}
.masthead-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 0.55rem;
}
.masthead h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    line-height: 1.15;
    color: #1a1a1a;
    margin: 0 0 0.5rem 0;
}
.masthead-sub {
    font-family: 'Source Serif 4', serif;
    font-size: 1.05rem;
    font-weight: 300;
    font-style: italic;
    color: #444;
    margin-bottom: 0;
    max-width: 640px;
}

/* ── Legend strip ── */
.legend-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin: 1.2rem 0 2rem 0;
    padding: 0.9rem 1rem;
    background: #f8f6f2;
    border: 1px solid #e0ddd8;
}
.legend-item {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #333;
}
.legend-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── Timeline shell ── */
.timeline-wrapper {
    position: relative;
    padding-left: 0;
}

/* ── Era divider ── */
.era-divider {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.5rem 0 1.2rem 0;
}
.era-divider-line {
    flex: 1;
    height: 1px;
    background: #c8c2b8;
}
.era-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #888;
    white-space: nowrap;
}

/* ── Event card ── */
.event-card {
    display: flex;
    gap: 0;
    margin-bottom: 1.4rem;
    position: relative;
}
.event-year-col {
    width: 80px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    padding-right: 1.2rem;
    padding-top: 0.1rem;
    position: relative;
}
.event-year-number {
    font-family: 'Playfair Display', serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #1a1a1a;
    line-height: 1;
}
.event-year-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    letter-spacing: 0.06em;
    color: #aaa;
    margin-top: 0.15rem;
}
.event-connector {
    position: absolute;
    right: -1px;
    top: 0.45rem;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border: 2px solid white;
    z-index: 2;
}
.event-spine {
    width: 2px;
    flex-shrink: 0;
    background: #d8d2c8;
    position: relative;
    margin-right: 1.2rem;
}
.event-body {
    flex: 1;
    min-width: 0;
    border-left: 3px solid;
    padding: 1rem 1.15rem 0.9rem 1.15rem;
    position: relative;
}
.event-body:hover {
    filter: brightness(0.97);
}
.event-cat-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
    padding: 0.15rem 0.5rem;
    border-radius: 2px;
}
.event-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.08rem;
    font-weight: 600;
    line-height: 1.3;
    color: #1a1a1a;
    margin-bottom: 0.5rem;
}
.event-desc {
    font-family: 'Source Serif 4', serif;
    font-size: 0.9rem;
    font-weight: 300;
    line-height: 1.7;
    color: #333;
    margin-bottom: 0.65rem;
}
.event-topics {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-bottom: 0.6rem;
}
.topic-pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.08em;
    color: #666;
    border: 1px solid #ccc;
    padding: 0.1rem 0.45rem;
    border-radius: 20px;
}
.event-source-link {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.06em;
    color: #888;
    text-decoration: none;
    border-bottom: 1px dotted #ccc;
    display: inline-block;
}
.event-source-link:hover {
    color: #333;
    border-bottom-color: #888;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #f4f1ec;
    border-right: 1px solid #e0ddd8;
}
section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}
.sidebar-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 0.2rem;
}
.sidebar-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 1.2rem;
}
.stat-box {
    background: white;
    border: 1px solid #e0ddd8;
    padding: 0.6rem 0.8rem;
    margin-bottom: 0.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #666;
}
.stat-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #1a1a1a;
}

/* ── Streamlit widget overrides ── */
div[data-testid="stMultiSelect"] label,
div[data-testid="stCheckbox"] label,
div.stSelectbox label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #555 !important;
}

/* ── Result count ── */
.result-count {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #e8e4de;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: #999;
    font-family: 'Source Serif 4', serif;
    font-style: italic;
}

/* ── Footer ── */
.timeline-footer {
    border-top: 1px solid #e0ddd8;
    margin-top: 3rem;
    padding-top: 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.08em;
    color: #aaa;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-header">Filter & Explore</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Berkeley Unified Timeline</div>', unsafe_allow_html=True)

    # Category filter
    all_categories = sorted({e["category"] for e in events})
    selected_cats = st.multiselect(
        "Category",
        options=all_categories,
        default=all_categories,
        help="Filter by event category"
    )

    # Decade filter
    all_decades = sorted({(e["year"] // 10) * 10 for e in events})
    decade_labels = [f"{d}s" for d in all_decades]
    selected_decade_labels = st.multiselect(
        "Decade",
        options=decade_labels,
        default=decade_labels,
    )
    selected_decades = {int(d[:-1]) for d in selected_decade_labels}

    # Topic filter
    all_topics = sorted({t for e in events for t in e["topics"]})
    topic_search = st.multiselect(
        "Topic",
        options=all_topics,
        default=[],
        placeholder="All topics",
    )

    st.divider()

    # Stats
    st.markdown("**Dataset**", help="Summary statistics")
    span_start = min(e["year"] for e in events)
    span_end   = max(e["year"] for e in events)

    for label, value in [
        ("Total Events", len(events)),
        ("Year Span", f"{span_start}–{span_end}"),
        ("Categories", len(all_categories)),
        ("Topics", len(all_topics)),
    ]:
        st.markdown(f"""
        <div class="stat-box">
            <span class="stat-label">{label}</span>
            <span class="stat-value">{value}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""
    <div style="font-family:'JetBrains Mono',monospace; font-size:0.58rem; color:#aaa; line-height:1.7; letter-spacing:0.05em;">
    Sources include the U.S. Commission on Civil Rights, California Dept. of Justice, City of Berkeley, and the Othering & Belonging Institute.
    </div>
    """, unsafe_allow_html=True)

# ── Filter events ─────────────────────────────────────────────────────────────
def filter_events(events, cats, decades, topics):
    result = []
    for e in events:
        if e["category"] not in cats:
            continue
        if (e["year"] // 10) * 10 not in decades:
            continue
        if topics and not any(t in e["topics"] for t in topics):
            continue
        result.append(e)
    return result

filtered = filter_events(events, selected_cats, selected_decades, topic_search)

# ── Masthead ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="masthead">
    <div class="masthead-eyebrow">Berkeley Unified School District · Historical Record</div>
    <h1>Race, School &amp; Community<br>in Berkeley, 1850–2024</h1>
    <p class="masthead-sub">A documentary timeline tracing how law, housing, organizing, and institution-building have shaped educational opportunity across 174 years.</p>
</div>
""", unsafe_allow_html=True)

# ── Legend ────────────────────────────────────────────────────────────────────
legend_html = '<div class="legend-strip">'
for cat, cfg in CATEGORY_CONFIG.items():
    legend_html += f"""
    <div class="legend-item">
        <div class="legend-dot" style="background:{cfg['color']};"></div>
        {cfg['icon']}&nbsp;{cfg['label']}
    </div>"""
legend_html += "</div>"
st.markdown(legend_html, unsafe_allow_html=True)

# ── Result count ──────────────────────────────────────────────────────────────
st.markdown(
    f'<div class="result-count">Showing {len(filtered)} of {len(events)} events</div>',
    unsafe_allow_html=True
)

# ── Timeline render ───────────────────────────────────────────────────────────
def get_era(year):
    if year < 1900: return ("1850–1899", "Foundations of Inequality")
    if year < 1950: return ("1900–1949", "Segregation Codified")
    if year < 1970: return ("1950–1969", "Civil Rights Era")
    if year < 1990: return ("1970–1989", "Integration & Backlash")
    if year < 2010: return ("1990–2009", "Documenting Disparity")
    return ("2010–Present", "Equity as Reckoning")

if not filtered:
    st.markdown('<div class="empty-state">No events match the current filters.<br>Try broadening your selection.</div>', unsafe_allow_html=True)
else:
    current_era = None

    for event in sorted(filtered, key=lambda e: e["year"]):
        era_key, era_name = get_era(event["year"])
        cfg = CATEGORY_CONFIG.get(event["category"], CATEGORY_CONFIG["National"])

        # Era divider
        if era_key != current_era:
            current_era = era_key
            st.markdown(f"""
            <div class="era-divider">
                <div class="era-divider-line"></div>
                <div class="era-label">{era_key} · {era_name}</div>
                <div class="era-divider-line"></div>
            </div>
            """, unsafe_allow_html=True)

        # Date display
        start_year = event["start_date"].split("/")[0]
        end_year   = event["end_date"].split("/")[0]
        year_display = start_year if start_year == end_year else f"{start_year}–{end_year}"

        # Topics pills
        topic_pills = "".join(
            f'<span class="topic-pill">{t}</span>'
            for t in event["topics"]
        )

        # Source
        source_html = ""
        if event.get("source_url") and event.get("source_citation"):
            short = event["source_citation"][:70] + ("…" if len(event["source_citation"]) > 70 else "")
            source_html = f'<a class="event-source-link" href="{event["source_url"]}" target="_blank" rel="noopener">↗ {short}</a>'

        card_html = f"""
        <div class="event-card">
            <div class="event-year-col">
                <div class="event-year-number">{year_display}</div>
                <div class="event-year-sub">{event["category"].upper()}</div>
                <div class="event-connector" style="background:{cfg['color']};"></div>
            </div>
            <div class="event-spine"></div>
            <div class="event-body" style="background:{cfg['bg']}; border-left-color:{cfg['border']};">
                <div class="event-cat-tag" style="background:{cfg['color']}18; color:{cfg['color']};">
                    {cfg['icon']}&nbsp;{cfg['label']}
                </div>
                <div class="event-title">{event['title']}</div>
                <div class="event-desc">{event['description']}</div>
                <div class="event-topics">{topic_pills}</div>
                {source_html}
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="timeline-footer">
    UC Berkeley Public Policy Data Lab · BUSD Timeline Project · Sources archived in events.json
</div>
""", unsafe_allow_html=True)
