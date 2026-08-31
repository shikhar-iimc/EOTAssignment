import streamlit as st
import plotly.graph_objects as go
from data import NODES, EDGES, SOURCES, PANEL, TEXT, GREY, RUST, GOLD, STEEL, SAGE
from styles import inject_base_styles, eyebrow, subtitle, tag, citation_line

st.set_page_config(page_title="Relationship Map", layout="wide")
inject_base_styles()

eyebrow("SUPPORTING EVIDENCE - THE FULL ECOSYSTEM")
st.title("Relationship Map")
subtitle("The documented contracts and partnerships connecting Palantir, Google, Anthropic, and their infrastructure and state clients")

st.markdown(
    """
    <div class="disclaimer-box">
    <span class="tag tag-fact">VERIFIED FACT</span> Every connection shown is a publicly reported
    contract, partnership, or dispute, not an inference, drawn primarily from a April 2026 research
    factsheet mapping Palantir's technology ecosystem and current defense-technology reporting on the
    Anthropic-DoD dispute. Node positions are laid out for readability only and carry no meaning.
    Click and drag nodes to rearrange the layout; hover any node or line for detail.
    </div>
    """,
    unsafe_allow_html=True,
)

# Wider layout: infrastructure providers on the outer ring, the three focal
# AI labs in the middle band, state/institutional clients on the bottom.
POS = {
    "Microsoft": (0.5, 4.2),
    "NVIDIA": (3.5, 4.2),
    "Amazon (AWS)": (7.0, 4.2),
    "Anthropic": (1.5, 2.0),
    "Palantir": (4.5, 2.0),
    "Google": (7.5, 2.0),
    "OpenAI": (5.8, 0.2),
    "U.S. DoD": (4.5, -1.8),
    "Israel (IDF)": (7.0, -3.4),
    "ICE / DHS": (4.5, -3.8),
    "UK NHS": (2.0, -3.4),
}
NODE_COLOR = {
    "Anthropic": SAGE, "Palantir": RUST, "Google": GOLD, "OpenAI": "#C9CDD3",
    "Microsoft": STEEL, "NVIDIA": "#8FBB8C", "Amazon (AWS)": "#E8A33D",
    "U.S. DoD": STEEL, "Israel (IDF)": "#8a8a8a", "ICE / DHS": "#8a8a8a", "UK NHS": "#8a8a8a",
}
NODE_SIZE = {
    "Anthropic": 52, "Palantir": 58, "Google": 52, "OpenAI": 46,
    "Microsoft": 40, "NVIDIA": 40, "Amazon (AWS)": 40,
    "U.S. DoD": 50, "Israel (IDF)": 34, "ICE / DHS": 34, "UK NHS": 34,
}

fig = go.Figure()

edge_style = {
    "partnership": dict(dash="solid", width=3, color=SAGE),
    "partnership (disrupted)": dict(dash="dot", width=3, color=RUST),
    "partnership (emerging)": dict(dash="dash", width=2, color="#C9CDD3"),
    "contract": dict(dash="solid", width=2.2, color=STEEL),
    "contract+dispute": dict(dash="dot", width=3.5, color=RUST),
    "contract (past+present)": dict(dash="dash", width=2.2, color=GOLD),
    "contract (contested)": dict(dash="dashdot", width=2.2, color=RUST),
    "contract (expanded)": dict(dash="solid", width=2.2, color="#C9CDD3"),
    "infrastructure": dict(dash="solid", width=1.4, color=GREY),
}

for (a, b, label, kind, src_key) in EDGES:
    x0, y0 = POS[a]
    x1, y1 = POS[b]
    style = edge_style.get(kind, dict(dash="solid", width=2, color=GREY))
    src = SOURCES.get(src_key)
    hover = f"<b>{a} to {b}</b><br>{label}" + (f"<br><i>Source: {src['label']}</i>" if src else "")
    fig.add_trace(go.Scatter(
        x=[x0, x1], y=[y0, y1], mode="lines",
        line=dict(color=style["color"], width=style["width"], dash=style["dash"]),
        hovertemplate=hover + "<extra></extra>",
        showlegend=False, opacity=0.75,
    ))

for node, (x, y) in POS.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y], mode="markers+text",
        marker=dict(size=NODE_SIZE.get(node, 40), color=NODE_COLOR.get(node, STEEL),
                    line=dict(color=TEXT, width=2)),
        text=[f"<b>{node}</b>"], textposition="bottom center",
        textfont=dict(size=12.5, color=TEXT, family="IBM Plex Mono"),
        hovertemplate=f"<b>{node}</b><extra></extra>",
        showlegend=False,
    ))

fig.update_layout(
    height=780,
    plot_bgcolor=PANEL, paper_bgcolor=PANEL,
    xaxis=dict(visible=False, range=[-1, 9], fixedrange=False),
    yaxis=dict(visible=False, range=[-5, 5.5], fixedrange=False),
    margin=dict(l=10, r=10, t=10, b=10),
    hoverlabel=dict(bgcolor="#12181F", font_size=12, font_color=TEXT, bordercolor=STEEL, align="left"),
    dragmode="pan",
)

st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True, "displayModeBar": True})

st.markdown(
    """
    <span style="font-family:'IBM Plex Mono',monospace; font-size:0.78rem; color:#9AA5AD;">
    LINE KEY &nbsp;&nbsp;
    <span style="color:#8FBB8C;">&#9473;&#9473;&#9473;</span> active partnership &nbsp;
    <span style="color:#D9663B;">&#8231;&#8231;&#8231;</span> disrupted / under dispute &nbsp;
    <span style="color:#C9CDD3;">&#8213;&#8213;&#8213;</span> emerging &nbsp;
    <span style="color:#7FA8C9;">&#9473;&#9473;&#9473;</span> standard contract &nbsp;
    <span style="color:#9AA5AD;">&#9473;&#9473;&#9473;</span> shared infrastructure
    </span>
    """,
    unsafe_allow_html=True,
)

st.divider()

st.header("All Documented Relationships")
for (a, b, label, kind, src_key) in EDGES:
    src = SOURCES.get(src_key)
    src_html = (
        f'<br><span class="source-pill">SOURCE: <a href="{src["url"]}" target="_blank">{src["label"]}</a></span>'
        if src else
        '<br><span class="source-pill">SOURCE: widely reported; see essay reference list</span>'
    )
    st.markdown(
        f"""
        <div class="fact-card">
        <b>{a}</b> &#8596; <b>{b}</b> <span style="color:#9AA5AD; font-size:0.78rem;">[{kind}]</span><br>
        {label}
        {src_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

tag("interp")
st.header("What This Map Is Actually Showing")
st.markdown(
    "Campolo and Crawford's phrase for a system like this one, **power without responsibility**, "
    "describes the graph above precisely: no single node bears the accountability the fused system "
    "as a whole exercises. The course's own account of the many-hands problem explains why this "
    "persists rather than resolving. When the DoD ordered Claude removed from Maven and Palantir "
    "began substituting other suppliers, the chain of design and operation fragmented further, "
    "making the question \"who is responsible\" harder to answer precisely as the systems "
    "accelerated."
)
citation_line(
    "Alex Campolo and Kate Crawford", "2020",
    "Enchanted Determinism: Power without Responsibility in Artificial Intelligence",
    "Engaging Science, Technology, and Society, 6, 1-19"
)
