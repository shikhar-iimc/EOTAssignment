"""styles.py — shared CSS injected on every page for a consistent, non-default look."""

import streamlit as st
from data import INK, PAPER, PAPER_DARK, RUST, GOLD, STEEL, SAGE, GREY, LINE


def inject_base_styles():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

        html, body, [class*="css"] {{
            font-family: 'IBM Plex Sans', sans-serif;
        }}

        .stApp {{
            background-color: {PAPER};
        }}

        h1, h2, h3 {{
            font-family: 'Source Serif 4', serif !important;
            color: {INK} !important;
        }}

        h1 {{
            border-bottom: 3px solid {RUST};
            padding-bottom: 0.3rem;
        }}

        p, li, span, label {{
            color: {INK};
        }}

        .eyebrow {{
            font-family: 'IBM Plex Mono', monospace;
            letter-spacing: 0.12em;
            font-size: 0.72rem;
            font-weight: 600;
            color: {RUST};
            text-transform: uppercase;
        }}

        .subtitle {{
            font-family: 'Source Serif 4', serif;
            font-style: italic;
            color: {STEEL};
            font-size: 1.05rem;
        }}

        .fact-card {{
            background-color: {PAPER_DARK};
            border-left: 4px solid {RUST};
            border-radius: 4px;
            padding: 0.85rem 1.1rem;
            margin-bottom: 0.7rem;
        }}

        .fact-date {{
            font-family: 'IBM Plex Mono', monospace;
            font-weight: 600;
            font-size: 0.78rem;
            color: {RUST};
        }}

        .quote-box {{
            background-color: {PAPER_DARK};
            border-left: 5px solid {GOLD};
            border-radius: 4px;
            padding: 1.1rem 1.3rem;
            margin: 1rem 0 1.4rem 0;
            font-family: 'Source Serif 4', serif;
            font-style: italic;
            font-size: 1.08rem;
            color: {INK};
        }}

        .quote-attr {{
            display: block;
            margin-top: 0.5rem;
            font-family: 'IBM Plex Sans', sans-serif;
            font-style: normal;
            font-size: 0.82rem;
            color: {GREY};
        }}

        .tag {{
            display: inline-block;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.68rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            padding: 0.15rem 0.55rem;
            border-radius: 3px;
            margin-right: 0.35rem;
        }}

        .tag-fact {{ background-color: #E3E8EA; color: {STEEL}; }}
        .tag-interp {{ background-color: #F3EAD3; color: {GOLD}; }}
        .tag-primary {{ background-color: #F4E4DE; color: {RUST}; }}

        .source-pill {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            color: {GREY};
        }}

        .chart-frame {{
            border: 1px solid {LINE};
            border-radius: 6px;
            padding: 0.6rem;
            background-color: {PAPER_DARK};
        }}

        .disclaimer-box {{
            background-color: #F4E4DE;
            border: 1px solid {RUST};
            border-radius: 5px;
            padding: 0.8rem 1.1rem;
            font-size: 0.85rem;
            color: {INK};
            margin-bottom: 1.2rem;
        }}

        hr {{
            border-color: {LINE};
        }}

        a {{
            color: #1155CC;
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background-color: {INK};
        }}
        section[data-testid="stSidebar"] * {{
            color: {PAPER} !important;
        }}
        section[data-testid="stSidebar"] a {{
            color: {GOLD} !important;
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
    attr_html = f'<span class="quote-attr">\u2014 {attribution}</span>' if attribution else ""
    st.markdown(f'<div class="quote-box">\u201c{text}\u201d{attr_html}</div>', unsafe_allow_html=True)


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
    return f'<span class="source-pill">Source: <a href="{s["url"]}" target="_blank">{s["label"]}</a></span>'
