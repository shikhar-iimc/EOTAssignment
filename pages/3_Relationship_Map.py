import streamlit as st
import plotly.graph_objects as go
import numpy as np
from data import NODES, EDGES, SOURCES, COMPANY_COLOR, PAPER_DARK, INK, GREY, RUST, GOLD, STEEL, SAGE
from styles import inject_base_styles, eyebrow, subtitle, tag

st.set_page_config(page_title="Relationship Map", page_icon="\U0001F517", layout="wide")
inject_base_styles()

eyebrow("SUPPORTING EVIDENCE \u2014 WHO CONTRACTS WITH WHOM")
st.title("Relationship Map")
subtitle("The documented contracts and partnerships connecting all three companies to state clients")

st.markdown(
    """
    <div class="disclaimer-box">
    <span class="tag tag-fact">VERIFIED FACT</span> Every connection shown is a publicly reported
    contract, partnership, or dispute \u2014 not an inference. Node positions are laid out for
    readability only and carry no meaning. Hover an edge or node for detail; click a source link
    to verify.
    </div>
    """,
    unsafe_allow_html=True,
)

# Manual layout — hand-placed for clarity rather than a force-directed algorithm,
# since there are few enough nodes that a deliberate layout reads better.
POS = {
    "Anthropic": (0, 2),
    "Palantir": (2, 2),
    "Google": (4, 2),
    "U.S. DoD": (2, 0),
    "Israel (IDF)": (3.6, -1.6),
    "ICE / DHS": (2, -2.2),
    "UK NHS": (0.4, -1.6),
}
NODE_COLOR = {
    "Anthropic": SAGE, "Palantir": RUST, "Google": GOLD,
    "U.S. DoD": STEEL, "Israel (IDF)": "#8a8a8a", "ICE / DHS": "#8a8a8a", "UK NHS": "#8a8a8a",
}

fig = go.Figure()

# Edges
edge_style = {
    "partnership": dict(dash="solid", width=3),
    "contract": dict(dash="solid", width=2),
    "contract+dispute": dict(dash="dot", width=3),
    "contract (past+present)": dict(dash="dash", width=2),
    "contract (contested)": dict(dash="dashdot", width=2),
}
for (a, b, label, kind, src_key) in EDGES:
    x0, y0 = POS[a]
    x1, y1 = POS[b]
    style = edge_style.get(kind, dict(dash="solid", width=2))
    src = SOURCES.get(src_key)
    hover = label + (f"<br><i>Source: {src['label']}</i>" if src else "")
    fig.add_trace(go.Scatter(
        x=[x0, x1], y=[y0, y1], mode="lines",
        line=dict(color=INK, width=style["width"], dash=style["dash"]),
        hovertemplate=hover + "<extra></extra>",
        showlegend=False, opacity=0.55,
    ))
    # midpoint label
    fig.add_annotation(x=(x0+x1)/2, y=(y0+y1)/2, text="", showarrow=False)

# Nodes
for node, (x, y) in POS.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y], mode="markers+text",
        marker=dict(size=46, color=NODE_COLOR.get(node, STEEL), line=dict(color=INK, width=2.2)),
        text=[f"<b>{node}</b>"], textposition="bottom center",
        textfont=dict(size=12.5, color=INK),
        hovertemplate=f"<b>{node}</b><extra></extra>",
        showlegend=False,
    ))

fig.update_layout(
    height=560,
    plot_bgcolor=PAPER_DARK, paper_bgcolor=PAPER_DARK,
    xaxis=dict(visible=False, range=[-1, 5]),
    yaxis=dict(visible=False, range=[-3.2, 3]),
    margin=dict(l=10, r=10, t=10, b=10),
    hoverlabel=dict(bgcolor="white", font_size=12, align="left"),
)

st.plotly_chart(fig, use_container_width=True)
st.caption("Line style indicates relationship type: solid = active partnership/contract, dotted = contract under active dispute, dashed = past contract or renewed, dash-dot = contested/under public pressure. Hover any line for detail.")

st.divider()

st.header("All Documented Relationships")
for (a, b, label, kind, src_key) in EDGES:
    src = SOURCES.get(src_key)
    src_html = f'<br><span class="source-pill">Source: <a href="{src["url"]}" target="_blank">{src["label"]}</a></span>' if src else '<br><span class="source-pill">Source: widely reported; see essay reference list</span>'
    st.markdown(
        f"""
        <div class="fact-card">
        <b>{a}</b> \u2194 <b>{b}</b> <span style="color:{GREY}; font-size:0.8rem;">[{kind}]</span><br>
        {label}
        {src_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
