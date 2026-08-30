"""styles.py - shared CSS injected on every page. Dark, high-contrast,
operations-console aesthetic: monospace/technical type, no emoji, no em-dashes
in generated copy (hyphens or periods used instead)."""

import streamlit as st
from data import INK, PANEL, PANEL_LIGHT, RUST, GOLD, STEEL, SAGE, GREY, TEXT, LINE


def inject_base_styles():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'IBM Plex Sans', sans-serif;
        }}

        .stApp {{
            background-color: {INK} !important;
        }}

        /* Remove Streamlit's default colored decoration bar at the top of the page
           (the thin strip using primaryColor) - it reads as a template tell. */
        div[data-testid="stDecoration"] {{
            display: none !important;
        }}
        header[data-testid="stHeader"] {{
            background-color: {INK} !important;
            border-bottom: 1px solid {LINE};
        }}

        .block-container {{
            padding-top: 3.2rem;
            max-width: 1200px;
        }}

        h1, h2, h3, h4 {{
            font-family: 'IBM Plex Mono', monospace !important;
            color: {TEXT} !important;
            letter-spacing: 0.01em;
            font-weight: 600 !important;
        }}

        h1 {{
            border-bottom: 2px solid {RUST};
            padding-bottom: 0.5rem;
            text-transform: uppercase;
            font-size: 1.55rem !important;
            line-height: 1.35 !important;
            white-space: normal !important;
            overflow-wrap: break-word;
            word-break: break-word;
        }}

        h2 {{
            font-size: 1.3rem !important;
            margin-top: 1.6rem;
        }}

        p, li, span, label, div {{
            color: {TEXT};
        }}

        .stMarkdown p {{
            font-family: 'IBM Plex Sans', sans-serif;
            line-height: 1.65;
        }}

        .eyebrow {{
            font-family: 'IBM Plex Mono', monospace;
            letter-spacing: 0.16em;
            font-size: 0.72rem;
            font-weight: 600;
            color: {RUST};
            text-transform: uppercase;
            margin-bottom: 0.3rem;
        }}

        .subtitle {{
            font-family: 'IBM Plex Sans', sans-serif;
            color: {STEEL};
            font-size: 1.05rem;
            margin-bottom: 1.2rem;
        }}

        .fact-card {{
            background-color: {PANEL};
            border: 1px solid {LINE};
            border-left: 3px solid {RUST};
            border-radius: 3px;
            padding: 0.9rem 1.15rem;
            margin-bottom: 0.7rem;
            color: {TEXT};
        }}

        .fact-card b, .fact-card strong {{
            color: {TEXT};
        }}

        .fact-date {{
            font-family: 'IBM Plex Mono', monospace;
            font-weight: 600;
            font-size: 0.78rem;
            color: {RUST};
        }}

        .quote-box {{
            background-color: {PANEL};
            border: 1px solid {LINE};
            border-left: 4px solid {GOLD};
            border-radius: 3px;
            padding: 1.1rem 1.3rem;
            margin: 1rem 0 1.4rem 0;
            font-family: 'IBM Plex Sans', sans-serif;
            font-style: italic;
            font-size: 1.05rem;
            color: {TEXT};
        }}

        .quote-attr {{
            display: block;
            margin-top: 0.5rem;
            font-family: 'IBM Plex Mono', monospace;
            font-style: normal;
            font-size: 0.75rem;
            letter-spacing: 0.02em;
            color: {GREY};
        }}

        .tag {{
            display: inline-block;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.66rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            padding: 0.18rem 0.6rem;
            border-radius: 2px;
            margin-right: 0.35rem;
            text-transform: uppercase;
        }}

        .tag-fact {{ background-color: rgba(127,168,201,0.15); color: {STEEL}; border: 1px solid {STEEL}; }}
        .tag-interp {{ background-color: rgba(212,167,44,0.15); color: {GOLD}; border: 1px solid {GOLD}; }}
        .tag-primary {{ background-color: rgba(217,102,59,0.15); color: {RUST}; border: 1px solid {RUST}; }}

        .source-pill {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            color: {GREY};
        }}
        .source-pill a {{
            color: {STEEL};
        }}

        .chart-frame {{
            border: 1px solid {LINE};
            border-radius: 4px;
            padding: 0.7rem;
            background-color: {PANEL};
        }}

        .disclaimer-box {{
            background-color: {PANEL};
            border: 1px solid {RUST};
            border-radius: 3px;
            padding: 0.9rem 1.15rem;
            font-size: 0.86rem;
            color: {TEXT};
            margin-bottom: 1.3rem;
        }}

        .disclaimer-box .tag {{ margin-right: 0.3rem; }}

        hr {{
            border-color: {LINE};
        }}

        a {{
            color: {STEEL};
        }}

        section[data-testid="stSidebar"] {{
            background-color: #060a0d;
            border-right: 1px solid {LINE};
        }}
        section[data-testid="stSidebar"] * {{
            color: {TEXT} !important;
            font-family: 'IBM Plex Mono', monospace !important;
        }}
        section[data-testid="stSidebar"] a {{
            color: {GOLD} !important;
        }}

        button[data-baseweb="tab"] {{
            font-family: 'IBM Plex Mono', monospace !important;
            color: {GREY} !important;
        }}
        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {RUST} !important;
            border-bottom-color: {RUST} !important;
        }}

        .stTextInput input, .stMultiSelect div[data-baseweb="select"] {{
            background-color: {PANEL} !important;
            color: {TEXT} !important;
            border: 1px solid {LINE} !important;
            font-family: 'IBM Plex Mono', monospace !important;
        }}

        .stCaption, [data-testid="stCaptionContainer"] {{
            color: {GREY} !important;
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 0.75rem !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def eyebrow(text: str):
    st.markdown(f'<div class="eyebrow">{text}</div>', unsafe_allow_html=True)


def subtitle(text: str):
    st.markdown(f'<div class="subtitle">{text}</div>', unsafe_allow_html=True)


def quote_box(text: str, attribution: str = ""):
    attr_html = f'<span class="quote-attr">SOURCE: {attribution}</span>' if attribution else ""
    st.markdown(f'<div class="quote-box">"{text}"{attr_html}</div>', unsafe_allow_html=True)


def tag(kind: str):
    mapping = {
        "fact": ("tag-fact", "VERIFIED FACT"),
        "interp": ("tag-interp", "OUR INTERPRETATION"),
        "primary": ("tag-primary", "PRIMARY SOURCE"),
    }
    cls, label = mapping.get(kind, ("tag-fact", kind.upper()))
    st.markdown(f'<span class="tag {cls}">{label}</span>', unsafe_allow_html=True)


def source_link(src_dict, key):
    if key is None or key not in src_dict:
        return ""
    s = src_dict[key]
    return f'<span class="source-pill">SOURCE: <a href="{s["url"]}" target="_blank">{s["label"]}</a></span>'


def citation_line(author: str, year: str, title: str, venue: str = ""):
    """Renders a small, explicit author/year/title citation strip.
    Used wherever a specific academic reading underlies the page, since
    named citations (not just links) are what the professor wants to see."""
    venue_html = f', <i>{venue}</i>' if venue else ""
    st.markdown(
        f'<div style="font-family:\'IBM Plex Mono\',monospace; font-size:0.78rem; '
        f'color:#9AA5AD; border-left:2px solid #D4A72C; padding-left:0.6rem; margin:0.4rem 0 1rem 0;">'
        f'{author} ({year}). "{title}."{venue_html}</div>',
        unsafe_allow_html=True,
    )
