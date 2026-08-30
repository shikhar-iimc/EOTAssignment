import streamlit as st
from data import PROFILES, INK, RUST, GOLD, STEEL, SAGE, PAPER_DARK
from styles import inject_base_styles, eyebrow, subtitle, quote_box, tag

st.set_page_config(
    page_title="Ethics, Enabled and Constrained",
    page_icon="\u2726",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_base_styles()

# ---------------- HERO ----------------
eyebrow("ETHICS OF TECHNOLOGY \u2014 INTERACTIVE ESSAY SUPPLEMENT")
st.title("Ethics, Enabled and Constrained")
subtitle("Reading Palantir, Google, and Anthropic through the grammar of military AI narratives")

st.markdown(
    """
    <div class="disclaimer-box">
    <b>What this site is.</b> This is a companion to a written essay submitted for
    <i>Ethics of Technology and Its Relevance for Business</i> (IIM Calcutta). It organizes the same
    research interactively \u2014 a timeline, a theoretical framework, a relationship map, and the full
    primary-source manifesto \u2014 so the evidence behind the essay's argument can be explored directly.
    Content here is consistently labeled: <b>verified fact</b> (sourced, dated claims), <b>primary source</b>
    (original documents/quotes), and <b>our interpretation</b> (the essay's own analytical argument).
    Nothing on this site is a substitute for the essay itself, which is the graded submission.
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------------- THESIS ----------------
st.header("The Core Argument")
st.markdown(
    """
    The three companies are not best understood on a scale from ethical to unethical. What distinguishes
    them is **which ethical narrative each has adopted** \u2014 drawing on Irja Malmio's framework of
    *enabling* and *constraining* narratives from the original Project Maven debate \u2014 and **how durable
    that narrative has proven** once tested by competitive and geopolitical pressure.
    """
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"#### :orange[Palantir]")
    st.markdown("**Maintenance**, stated as ideology. A contested political choice presented as historical inevitability.")
with col2:
    st.markdown(f"#### :orange[Google]")
    st.markdown("**Disengagement \u2192 Maintenance.** Abandoned a 2018 constraint under pressure, in terms echoing its own 2018 arguments.")
with col3:
    st.markdown(f"#### :orange[Anthropic]")
    st.markdown("**Ambivalence.** A real, litigated line \u2014 explicitly conditional on what competitors do.")

st.divider()

# ---------------- NAVIGATION CARDS ----------------
st.header("Explore the Research")
st.caption("Use the sidebar to navigate, or jump in below.")

nav_items = [
    ("\U0001F5FA\uFE0F Narrative Framework", "Malmio's four-narrative quadrant, interactive \u2014 see where each company sits and why."),
    ("\U0001F4C5 Timeline", "Every dated event in the Anthropic\u2013DoD dispute and the wider story, sourced."),
    ("\U0001F517 Relationship Map", "Who contracts with whom \u2014 Palantir, Google, Anthropic, DoD, and other clients."),
    ("\U0001F3E2 Company Profiles", "Deep dives on each firm: key facts, quotes, and the essay's reading of each."),
    ("\U0001F4DC The Manifesto", "All 22 points of Palantir's 'Technological Republic' thread, searchable, linked to the primary source."),
    ("\U0001F4DA Sources", "Every citation used across the essay and this site, in one place."),
]
cols = st.columns(2)
for i, (title, desc) in enumerate(nav_items):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="fact-card">
            <b>{title}</b><br>
            <span style="font-size:0.88rem;">{desc}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ---------------- KEY QUOTE ----------------
st.header("The Sharpest Fact in the Whole Case")
quote_box(
    "In July 2024, Palantir announced a partnership to embed Anthropic's Claude directly into "
    "US government intelligence and defense operations \u2014 a full year before Anthropic's public "
    "legal battle with the Department of Defense over the ethical limits of that same military AI use.",
    "Discussed in Section 4 of the essay; see Timeline and Relationship Map"
)
st.markdown(
    "The most vocal advocate of military AI and its most vocal domestic restrainer are, "
    "through a single commercial partnership, running the same underlying software."
)

st.divider()
st.caption("Built as a research supplement by Shikhar Sharma \u00b7 IIM Calcutta, Term IV, AY 2026\u201327 \u00b7 Ethics of Technology and Its Relevance for Business")
