import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data import TIMELINE, SOURCES, COMPANY_COLOR, PANEL, TEXT, GREY, STEEL
from styles import inject_base_styles, eyebrow, subtitle

st.set_page_config(page_title="Timeline", page_icon=None, layout="wide")
inject_base_styles()

eyebrow("SECTIONS 2-4 OF THE ESSAY - THE FACTUAL RECORD")
st.title("Timeline of Events")
subtitle("Every dated event referenced in the essay and its research supplement, in one place")

st.markdown(
    """
    <div class="disclaimer-box">
    <span class="tag tag-fact">VERIFIED FACT</span> Every entry below is a dated, sourced event.
    Filter by company using the sidebar control, and follow a source link to verify directly.
    </div>
    """,
    unsafe_allow_html=True,
)

all_actors = sorted(set(item["actor"] for item in TIMELINE))
selected = st.sidebar.multiselect("Filter by company", all_actors, default=all_actors)

filtered = [item for item in TIMELINE if item["actor"] in selected]
filtered = sorted(filtered, key=lambda x: x["date"])

df = pd.DataFrame(filtered)
if not df.empty:
    df["date_parsed"] = pd.to_datetime(df["date"], format="%Y-%m")
    fig = go.Figure()
    for actor in sorted(df["actor"].unique()):
        sub = df[df["actor"] == actor]
        fig.add_trace(go.Scatter(
            x=sub["date_parsed"], y=[actor] * len(sub),
            mode="markers",
            marker=dict(size=16, color=COMPANY_COLOR.get(actor, STEEL), line=dict(color=TEXT, width=1.5)),
            text=sub["event"],
            hovertemplate="<b>%{x|%b %Y}</b><br>%{text}<extra></extra>",
            name=actor,
        ))
    fig.update_layout(
        height=300,
        plot_bgcolor=PANEL, paper_bgcolor=PANEL,
        font=dict(color=TEXT, family="IBM Plex Mono"),
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(showgrid=True, gridcolor="#2A343D", title=None, color=TEXT),
        yaxis=dict(showgrid=False, title=None, color=TEXT),
        showlegend=False,
        hoverlabel=dict(bgcolor="#12181F", font_size=12, font_color=TEXT, bordercolor=STEEL),
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

for item in filtered:
    src = SOURCES.get(item["src"]) if item["src"] else None
    src_html = ""
    if src:
        src_html = f'<br><span class="source-pill">SOURCE: <a href="{src["url"]}" target="_blank">{src["label"]}</a></span>'
    st.markdown(
        f"""
        <div class="fact-card">
        <span class="fact-date">{item['date']}</span> &middot; <b>{item['actor']}</b><br>
        {item['event']}
        {src_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

if not filtered:
    st.info("No events match the current filter.")
