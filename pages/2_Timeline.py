import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data import TIMELINE, SOURCES, COMPANY_COLOR, PAPER_DARK, INK, GREY, STEEL
from styles import inject_base_styles, eyebrow, subtitle, tag

st.set_page_config(page_title="Timeline", page_icon="\U0001F4C5", layout="wide")
inject_base_styles()

eyebrow("SECTIONS 2\u20134 OF THE ESSAY \u2014 THE FACTUAL RECORD")
st.title("Timeline of Events")
subtitle("Every dated event referenced in the essay, in one place")

st.markdown(
    """
    <div class="disclaimer-box">
    <span class="tag tag-fact">VERIFIED FACT</span> Every entry below is a dated, sourced event.
    Filter by company using the sidebar control, and click a source link to verify directly.
    </div>
    """,
    unsafe_allow_html=True,
)

all_actors = sorted(set(item["actor"] for item in TIMELINE))
selected = st.sidebar.multiselect("Filter by company", all_actors, default=all_actors)

filtered = [item for item in TIMELINE if item["actor"] in selected]
filtered = sorted(filtered, key=lambda x: x["date"])

# ---------------- Plotly timeline strip ----------------
df = pd.DataFrame(filtered)
if not df.empty:
    df["date_parsed"] = pd.to_datetime(df["date"], format="%Y-%m")
    fig = go.Figure()
    for actor in sorted(df["actor"].unique()):
        sub = df[df["actor"] == actor]
        fig.add_trace(go.Scatter(
            x=sub["date_parsed"], y=[actor] * len(sub),
            mode="markers",
            marker=dict(size=16, color=COMPANY_COLOR.get(actor, STEEL), line=dict(color=INK, width=1.5)),
            text=sub["event"],
            hovertemplate="<b>%{x|%b %Y}</b><br>%{text}<extra></extra>",
            name=actor,
        ))
    fig.update_layout(
        height=260,
        plot_bgcolor=PAPER_DARK, paper_bgcolor=PAPER_DARK,
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(showgrid=True, gridcolor="#DDD6C8", title=None),
        yaxis=dict(showgrid=False, title=None),
        showlegend=False,
        hoverlabel=dict(bgcolor="white", font_size=12),
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------- Detailed cards ----------------
for item in filtered:
    src = SOURCES.get(item["src"]) if item["src"] else None
    src_html = ""
    if src:
        src_html = f'<br><span class="source-pill">Source: <a href="{src["url"]}" target="_blank">{src["label"]}</a></span>'
    st.markdown(
        f"""
        <div class="fact-card">
        <span class="fact-date">{item['date']}</span> \u00b7 <b>{item['actor']}</b><br>
        {item['event']}
        {src_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

if not filtered:
    st.info("No events match the current filter.")
