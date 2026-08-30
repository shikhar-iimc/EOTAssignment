import streamlit as st
from data import PROFILES
from styles import inject_base_styles, eyebrow, subtitle, quote_box, tag

st.set_page_config(
    page_title="Same Stack, Different Story",
    
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_base_styles()

eyebrow("ETHICS OF TECHNOLOGY - INTERACTIVE ESSAY SUPPLEMENT")
st.title("Same Stack, Different Story")
subtitle("Palantir, Google, and Anthropic on military AI: reading the grammar of enabling and constraining narratives")

st.markdown(
    """
    <div class="disclaimer-box">
    <b>What this site is.</b> This is a companion to a written essay submitted for
    <i>Ethics of Technology and Its Relevance for Business</i> (IIM Calcutta). It organizes the
    research interactively: a timeline, a theoretical framework, a relationship map, and the full
    primary-source manifesto, so the evidence behind the essay's argument can be explored directly.
    The content is consistently labeled as: <b>verified fact</b> (sourced, dated claims), <b>primary
    source</b> (original documents and quotes), and <b>our interpretation</b> (the essay's
    analytical argument).
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

st.header("The Core Argument")
st.markdown(
    """
    The three companies are not best understood on a scale from ethical to unethical. What distinguishes
    them is which ethical narrative each has adopted, drawing on Irja Malmio's framework of
    <i>enabling</i> and <i>constraining</i> narratives from the original Project Maven debate, and how
    durable that narrative has proven once tested by competitive and geopolitical pressure.
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### PALANTIR")
    st.markdown("**Maintenance**, stated as ideology. A contested political choice presented as historical inevitability.")
with col2:
    st.markdown("#### GOOGLE")
    st.markdown("**Disengagement to Maintenance.** Abandoned a 2018 constraint under pressure, in terms echoing its own 2018 arguments.")
with col3:
    st.markdown("#### ANTHROPIC")
    st.markdown("**Ambivalence.** A real, litigated line, explicitly conditional on what competitors do.")

st.divider()

st.header("Explore the Research")
st.caption("Use the sidebar to navigate, or jump in below.")

nav_items = [
    ("NARRATIVE FRAMEWORK", "Malmio's four-narrative quadrant, interactive. See where each company sits and why."),
    ("TIMELINE", "Every dated event across the Anthropic-DoD dispute and the wider ecosystem, sourced."),
    ("RELATIONSHIP MAP", "Who contracts with whom: Palantir, Google, Anthropic, OpenAI, Microsoft, NVIDIA, and state clients."),
    ("COMPANY PROFILES", "Deep dives on each firm: key facts, quotes, and the essay's reading of each."),
    ("THE MANIFESTO", "All 22 points of Palantir's 'Technological Republic' thread, searchable, linked to the primary source."),
    ("SOURCES", "Every citation used across the essay and this site, in one place."),
]
cols = st.columns(2)
for i, (nav_title, desc) in enumerate(nav_items):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="fact-card">
            <span style="font-family:'IBM Plex Mono',monospace; font-weight:600; color:#D9663B; letter-spacing:0.04em; font-size:0.8rem;">{nav_title}</span><br>
            <span style="font-size:0.9rem;">{desc}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

st.header("The Sharpest Fact in the Whole Case")
quote_box(
    "In November 2024, Palantir announced a partnership to integrate Anthropic's Claude directly "
    "into its AI Platform and, through it, into the DoD's Maven Smart System, more than a year before "
    "Anthropic's public legal battle with the Department of Defense over the ethical limits of that "
    "same military AI use. Reporting from March 2026 indicates Claude, deployed through Maven, may have "
    "supported target prioritization during coordinated US-Israel strikes on Iran the same month "
    "Anthropic was fighting its supply chain risk designation in court.",
    "See Timeline and Relationship Map for full sourcing"
)
st.markdown(
    "The most vocal advocate of military AI and its most vocal domestic restrainer were, through a "
    "single commercial partnership, running the same underlying software, reportedly at the same moment "
    "that software was making live targeting recommendations."
)

st.divider()
st.caption("Built as a research supplement by Shikhar Sharma. IIM Calcutta, Term IV, AY 2026-27. Ethics of Technology and Its Relevance for Business.")
