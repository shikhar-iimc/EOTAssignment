import streamlit as st
import plotly.graph_objects as go
from data import PANEL, RUST, GOLD, STEEL, SAGE, TEXT, GREY, LINE
from styles import inject_base_styles, eyebrow, subtitle, tag, citation_line

st.set_page_config(page_title="Narrative Framework", layout="wide")
inject_base_styles()

eyebrow("SECTION 1 OF THE ESSAY - THEORETICAL FRAME")
st.title("Malmio's Four Narratives")
subtitle("An interactive map of the enabling and constraining narratives that structure military AI ethics")
citation_line(
    "Irja Malmio", "2023",
    "Ethics as an enabler and a constraint: Narratives on technology development and artificial intelligence in military affairs through the case of Project Maven",
    "Technology in Society, 72, 102193"
)

st.markdown(
    """
    <div class="disclaimer-box">
    <b>How to read this chart.</b> The quadrant structure (four narrative types, two axes) is
    Irja Malmio's published analytical framework <span class="tag tag-fact">VERIFIED FACT</span>.
    The exact position of each company marker within its quadrant is
    <span class="tag tag-interp">OUR INTERPRETATION</span>, a qualitative placement based on the
    evidence discussed in the essay, not a measured score.
    </div>
    """,
    unsafe_allow_html=True,
)

fig = go.Figure()

quadrants = [
    dict(x0=-5, x1=0, y0=0, y1=5, fillcolor="rgba(217,102,59,0.045)", label="ACCURACY", lx=-2.5, ly=4.3, color=RUST),
    dict(x0=0, x1=5, y0=0, y1=5, fillcolor="rgba(212,167,44,0.045)", label="MAINTENANCE", lx=2.5, ly=4.3, color=GOLD),
    dict(x0=-5, x1=0, y0=-5, y1=0, fillcolor="rgba(127,168,201,0.045)", label="DISENGAGEMENT", lx=-2.5, ly=-0.7, color=STEEL),
    dict(x0=0, x1=5, y0=-5, y1=0, fillcolor="rgba(143,187,140,0.045)", label="AMBIVALENCE", lx=2.5, ly=-0.7, color=SAGE),
]
for q in quadrants:
    fig.add_shape(type="rect", x0=q["x0"], x1=q["x1"], y0=q["y0"], y1=q["y1"],
                  fillcolor=q["fillcolor"], line=dict(color=q["color"], width=1), layer="below")
    fig.add_annotation(x=q["lx"], y=q["ly"], text=f"<b>{q['label']}</b>", showarrow=False,
                        font=dict(size=16, color=q["color"], family="IBM Plex Mono"))

descriptions = {
    "ACCURACY": "AI improves precision, reduces civilian harm.<br>Ethics = the solution to violence.",
    "MAINTENANCE": "Preserve the existing balance of power.<br>Techno-centric warfare as deterrence.",
    "DISENGAGEMENT": "Refuse outright. Some harms cannot be<br>offset by any gain in accuracy.",
    "AMBIVALENCE": "Accept AI for military ends, but insist<br>on limits, a line under constant pressure.",
}
desc_pos = {"ACCURACY": (-2.5, 3.55), "MAINTENANCE": (2.5, 1.75), "DISENGAGEMENT": (-2.5, -3.55), "AMBIVALENCE": (2.5, -3.9)}
for label, (dx, dy) in desc_pos.items():
    fig.add_annotation(x=dx, y=dy, text=descriptions[label], showarrow=False,
                        font=dict(size=11, color=TEXT, family="IBM Plex Sans"), align="center")

fig.add_shape(type="line", x0=-5, x1=5, y0=0, y1=0, line=dict(color=TEXT, width=1.5))
fig.add_shape(type="line", x0=0, x1=0, y0=-5, y1=5, line=dict(color=TEXT, width=1.5))
fig.add_annotation(x=0, y=5.35, text="<b>ENABLING</b>", showarrow=False, font=dict(size=13, color=RUST, family="IBM Plex Mono"))
fig.add_annotation(x=0, y=-5.35, text="<b>CONSTRAINING</b>", showarrow=False, font=dict(size=13, color=STEEL, family="IBM Plex Mono"))
fig.add_annotation(x=-5.5, y=0, text="CONSEQUENTIALIST", showarrow=False, textangle=-90, font=dict(size=10, color=GREY, family="IBM Plex Mono"))
fig.add_annotation(x=5.5, y=0, text="DEONTOLOGICAL", showarrow=False, textangle=90, font=dict(size=10, color=GREY, family="IBM Plex Mono"))

markers = [
    dict(x=2.9, y=3.7, name="Palantir", color=RUST,
         note="Maintenance stated as ideology. The manifesto explicitly recommends militarisation as historical necessity."),
    dict(x=3.6, y=0.65, name="Google (2025)", color=GOLD,
         note="Adopted the maintenance narrative in Feb 2025, echoing Eric Schmidt's 2018 warning almost verbatim."),
    dict(x=-1.4, y=-1.9, name="Google (2018)", color="#8a8a8a",
         note="The 2018 employee-driven disengagement narrative, later abandoned."),
    dict(x=1.4, y=-2.6, name="Anthropic", color=SAGE,
         note="A litigated line, but one its own CSO called conditional on competitor behaviour."),
]
for m in markers:
    fig.add_trace(go.Scatter(
        x=[m["x"]], y=[m["y"]], mode="markers+text",
        marker=dict(size=22, color=m["color"], line=dict(color=TEXT, width=2)),
        text=[f"<b>{m['name']}</b>"], textposition="bottom center",
        textfont=dict(size=12, color=TEXT, family="IBM Plex Mono"),
        hovertemplate=f"<b>{m['name']}</b><br>{m['note']}<extra></extra>",
        name=m["name"], showlegend=False,
    ))

fig.update_layout(
    xaxis=dict(range=[-6.2, 6.2], showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(range=[-6.2, 6.2], showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor=PANEL, paper_bgcolor=PANEL,
    height=620, margin=dict(l=20, r=20, t=20, b=20),
    hoverlabel=dict(bgcolor="#12181F", font_size=13, font_family="IBM Plex Mono", font_color=TEXT, bordercolor=STEEL),
)

st.plotly_chart(fig, use_container_width=True)
st.caption("Hover over a marker to see the reasoning behind its placement.")

st.divider()

st.header("The Underlying Concepts")
tab1, tab2, tab3, tab4 = st.tabs(["ACCURACY", "MAINTENANCE", "DISENGAGEMENT", "AMBIVALENCE"])
with tab1:
    tag("fact")
    st.markdown("**Enabling. Consequentialist.** AI improves the precision of military targeting and thereby reduces civilian harm, making development an ethical imperative rather than a moral risk. Rooted in the Cold War-era 'accuracy paradigm' in US military strategy.")
    st.markdown("Lucy Suchman's study of Project Maven contests this directly, arguing that automating target analysis \"can only serve to exacerbate military operations that are at once discriminatory and indiscriminate in their targeting, while remaining politically and legally unaccountable.\"")
    citation_line("Lucy Suchman", "2020", "Algorithmic Warfare and the Reinvention of Accuracy", "Critical Studies on Security, 8(2), 175-187")
with tab2:
    tag("fact")
    st.markdown("**Enabling. Consequentialist.** Developing AI capability is necessary to preserve an existing balance of power. Andrew Feenberg's warning applies directly: a society committed to a technological path will be 'inexorably transformed... dedicated to values such as efficiency and power.'")
    citation_line("Andrew Feenberg", "2017", "A Critical Theory of Technology")
with tab3:
    tag("fact")
    st.markdown("**Constraining. Deontological.** Some technologies must be refused outright because potential harms cannot be offset by any accuracy gain, a Kantian categorical prohibition. This was the 2018 Google employees' position.")
with tab4:
    tag("fact")
    st.markdown("**Constraining. Deontological.** Accepts military AI but insists on limits, while remaining exposed to the charge that any such line is, in Malmio's own words, **'a chimera'** under constant pressure to move. This is Anthropic's position.")

st.divider()
st.caption("Source: Malmio, I. (2023). Ethics as an enabler and a constraint. Technology in Society, 72, 102193. doi.org/10.1016/j.techsoc.2022.102193")

st.divider()

st.header("Human-in-the-Loop: A Principle, Not a Slogan")
citation_line(
    "Filippo Santoni de Sio and Jeroen van den Hoven", "2018",
    "Meaningful Human Control over Autonomous Systems: A Philosophical Account",
    "Frontiers in Robotics and AI, 5, 15"
)
st.markdown(
    """
    <div class="disclaimer-box">
    <span class="tag tag-fact">VERIFIED FACT</span> The EU AI Act and the corresponding American
    executive order define an AI system as software that, for human-defined objectives, produces
    outputs that influence its environment. Because objectives are human-defined, humans are
    necessarily present across the system's lifecycle, which is why "human-in-the-loop" governance
    is close to definitional rather than a voluntary add-on.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    "Santoni de Sio and van den Hoven specify two necessary conditions for a system to remain "
    "under meaningful human control: a **tracking** condition, under which the system responds to "
    "the moral reasons relevant to the humans designing and deploying it, and a **tracing** "
    "condition, under which any outcome can be traced back to at least one human in the chain of "
    "design and operation. Their term for what fails when both lapse is the **responsibility gap**."
)

tag("fact")
st.markdown("#### Does the principle hold under pressure?")
st.markdown(
    "Reporting by +972 Magazine and Local Call on Israel's Lavender AI-targeting system found "
    "officers devoting roughly **twenty seconds** to each machine-generated target, often only to "
    "confirm the target was male, with one officer describing having \"zero added value as a human, "
    "apart from being a stamp of approval,\" against a system with a reported **ten per cent error "
    "rate**. Shandler, Gross and Shereshevsky identify this as automation bias corroding oversight "
    "in high-stakes military decisions."
)
citation_line("Yuval Abraham", "2024", "\u2018Lavender\u2019: The AI Machine Directing Israel's Bombing Spree in Gaza", "+972 Magazine, April 3")
citation_line("Ryan Shandler, Michael L. Gross, and Yahli Shereshevsky", "2026", "Black Box Warfare: Human Judgment and Military Decision-Making in the Age of AI", "Journal of Conflict Resolution")
st.markdown(
    "On Santoni de Sio and van den Hoven's own terms, such a system may satisfy *tracing* (a human "
    "remains formally in the chain) while wholly failing *tracking* (whether real deliberation is "
    "happening). A restriction like Anthropic's constrains system architecture; it cannot by itself "
    "constrain the quality of the deliberation that architecture exists to protect."
)
