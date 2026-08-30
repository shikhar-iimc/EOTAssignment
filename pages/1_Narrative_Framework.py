import streamlit as st
import plotly.graph_objects as go
from data import PAPER_DARK, RUST, GOLD, STEEL, SAGE, INK, GREY, LINE
from styles import inject_base_styles, eyebrow, subtitle, tag

st.set_page_config(page_title="Narrative Framework", page_icon="\U0001F5FA\uFE0F", layout="wide")
inject_base_styles()

eyebrow("SECTION 1 OF THE ESSAY \u2014 THEORETICAL FRAME")
st.title("Malmio's Four Narratives")
subtitle("An interactive map of the enabling and constraining narratives that structure military AI ethics")

st.markdown(
    """
    <div class="disclaimer-box">
    <b>How to read this chart.</b> The quadrant structure (four narrative types, two axes) is
    Irja Malmio's published analytical framework <span class="tag tag-fact">VERIFIED FACT</span>.
    The exact position of each company marker within its quadrant is <span class="tag tag-interp">OUR INTERPRETATION</span> \u2014
    a qualitative placement based on the evidence discussed in the essay, not a measured score.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Build interactive quadrant with Plotly ----------------
fig = go.Figure()

# Quadrant backgrounds
quadrants = [
    dict(x0=-5, x1=0, y0=0, y1=5, fillcolor="#F4E4DE", label="ACCURACY", lx=-2.5, ly=4.3, color=RUST),
    dict(x0=0, x1=5, y0=0, y1=5, fillcolor="#F3EAD3", label="MAINTENANCE", lx=2.5, ly=4.3, color=GOLD),
    dict(x0=-5, x1=0, y0=-5, y1=0, fillcolor="#E3E8EA", label="DISENGAGEMENT", lx=-2.5, ly=-0.7, color=STEEL),
    dict(x0=0, x1=5, y0=-5, y1=0, fillcolor="#E7EBE2", label="AMBIVALENCE", lx=2.5, ly=-0.7, color=SAGE),
]
for q in quadrants:
    fig.add_shape(type="rect", x0=q["x0"], x1=q["x1"], y0=q["y0"], y1=q["y1"],
                   fillcolor=q["fillcolor"], line=dict(color=q["color"], width=2), layer="below")
    fig.add_annotation(x=q["lx"], y=q["ly"], text=f"<b>{q['label']}</b>", showarrow=False,
                        font=dict(size=16, color=q["color"], family="IBM Plex Sans"))

descriptions = {
    "ACCURACY": "AI improves precision, reduces civilian harm.<br>Ethics = the solution to violence.",
    "MAINTENANCE": "Preserve the existing balance of power.<br>Techno-centric warfare as deterrence.",
    "DISENGAGEMENT": "Refuse outright. Some harms cannot be<br>offset by any gain in accuracy.",
    "AMBIVALENCE": "Accept AI for military ends, but insist<br>on limits \u2014 a line under constant pressure.",
}
desc_pos = {"ACCURACY": (-2.5, 2.6), "MAINTENANCE": (2.5, 2.6), "DISENGAGEMENT": (-2.5, -2.6), "AMBIVALENCE": (2.5, -2.6)}
for label, (dx, dy) in desc_pos.items():
    fig.add_annotation(x=dx, y=dy, text=descriptions[label], showarrow=False,
                        font=dict(size=11.5, color=INK, family="IBM Plex Sans"), align="center")

# Axis lines
fig.add_shape(type="line", x0=-5, x1=5, y0=0, y1=0, line=dict(color=INK, width=1.5))
fig.add_shape(type="line", x0=0, x1=0, y0=-5, y1=5, line=dict(color=INK, width=1.5))
fig.add_annotation(x=0, y=5.35, text="<b>ENABLING</b>", showarrow=False, font=dict(size=13, color=RUST))
fig.add_annotation(x=0, y=-5.35, text="<b>CONSTRAINING</b>", showarrow=False, font=dict(size=13, color=STEEL))
fig.add_annotation(x=-5.5, y=0, text="CONSEQUENTIALIST", showarrow=False, textangle=-90, font=dict(size=10, color=GREY))
fig.add_annotation(x=5.5, y=0, text="DEONTOLOGICAL", showarrow=False, textangle=90, font=dict(size=10, color=GREY))

# Company markers (interpretive placement)
markers = [
    dict(x=2.6, y=3.3, name="Palantir", color=RUST, note="Maintenance stated as ideology \u2014 the manifesto explicitly recommends militarisation as historical necessity."),
    dict(x=1.4, y=1.0, name="Google (2025)", color=GOLD, note="Adopted the maintenance narrative in Feb 2025, echoing Eric Schmidt's 2018 warning almost verbatim."),
    dict(x=-1.7, y=-1.1, name="Google (2018)", color="#8a8a8a", note="The 2018 employee-driven disengagement narrative \u2014 later abandoned."),
    dict(x=2.3, y=-3.2, name="Anthropic", color=SAGE, note="A litigated line, but one its own CSO called conditional on competitor behaviour."),
]
for m in markers:
    fig.add_trace(go.Scatter(
        x=[m["x"]], y=[m["y"]], mode="markers+text",
        marker=dict(size=22, color=m["color"], line=dict(color=INK, width=2)),
        text=[f"<b>{m['name']}</b>"], textposition="bottom center",
        textfont=dict(size=12, color=INK, family="IBM Plex Sans"),
        hovertemplate=f"<b>{m['name']}</b><br>{m['note']}<extra></extra>",
        name=m["name"], showlegend=False,
    ))

fig.update_layout(
    xaxis=dict(range=[-6.2, 6.2], showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(range=[-6.2, 6.2], showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor=PAPER_DARK, paper_bgcolor=PAPER_DARK,
    height=620, margin=dict(l=20, r=20, t=20, b=20),
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="IBM Plex Sans"),
)

st.plotly_chart(fig, use_container_width=True)
st.caption("Hover over a marker to see the reasoning behind its placement.")

st.divider()

st.header("The Underlying Concepts")
tab1, tab2, tab3, tab4 = st.tabs(["Accuracy", "Maintenance", "Disengagement", "Ambivalence"])
with tab1:
    tag("fact")
    st.markdown("**Enabling \u00b7 Consequentialist.** AI improves the precision of military targeting and thereby reduces civilian harm — making development an ethical imperative rather than a moral risk. Rooted in the Cold War-era 'accuracy paradigm' in US military strategy.")
with tab2:
    tag("fact")
    st.markdown("**Enabling \u00b7 Consequentialist.** Developing AI capability is necessary to preserve an existing balance of power. Andrew Feenberg's warning applies directly: a society committed to a technological path will be 'inexorably transformed... dedicated to values such as efficiency and power.'")
with tab3:
    tag("fact")
    st.markdown("**Constraining \u00b7 Deontological.** Some technologies must be refused outright because potential harms cannot be offset by any accuracy gain — a Kantian categorical prohibition. This was the 2018 Google employees' position.")
with tab4:
    tag("fact")
    st.markdown("**Constraining \u00b7 Deontological.** Accepts military AI but insists on limits, while remaining exposed to the charge that any such line is, in Malmio's own words, **'a chimera'** under constant pressure to move. This is Anthropic's position.")

st.divider()
st.caption("Source: Malmio, I. (2023). Ethics as an enabler and a constraint: Narratives on technology development and artificial intelligence in military affairs through the case of Project Maven. *Technology in Society*, 72, 102193. \u2014 [doi.org/10.1016/j.techsoc.2022.102193](https://doi.org/10.1016/j.techsoc.2022.102193)")
