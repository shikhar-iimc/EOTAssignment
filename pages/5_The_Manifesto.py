import streamlit as st
from data import MANIFESTO_POINTS, SOURCES
from styles import inject_base_styles, eyebrow, subtitle, tag

st.set_page_config(page_title="The Manifesto", page_icon=None, layout="wide")
inject_base_styles()

eyebrow("PRIMARY SOURCE - DISCUSSED IN SECTION 2 OF THE ESSAY")
st.title("Palantir's 'Technological Republic' Manifesto")
subtitle("All 22 points, verbatim, with the essay's thematic categorisation")

src = SOURCES["palantir_manifesto"]
st.markdown(
    f"""
    <div class="disclaimer-box">
    <span class="tag tag-primary">PRIMARY SOURCE</span> The 22 points below are quoted directly from
    Palantir's official account. Point text is verbatim (light paraphrase only where the original ran
    long); the essay quotes only a handful directly. All 22 are reproduced here for reference.
    Original source: <a href="{src['url']}" target="_blank">{src['label']}</a>. The claims underlying
    each point are Palantir's own; the thematic label in the right-hand column is the essay's analysis,
    not Palantir's.
    </div>
    """,
    unsafe_allow_html=True,
)

search = st.text_input("Search the manifesto (searches point text and theme)", "")

themes = sorted(set(p[3] for p in MANIFESTO_POINTS))
selected_themes = st.multiselect("Filter by theme", themes, default=[])

filtered = MANIFESTO_POINTS
if search:
    s = search.lower()
    filtered = [p for p in filtered if s in p[1].lower() or s in p[2].lower() or s in p[3].lower()]
if selected_themes:
    filtered = [p for p in filtered if p[3] in selected_themes]

st.caption(f"Showing {len(filtered)} of {len(MANIFESTO_POINTS)} points.")

for (num, headline, body, theme) in filtered:
    contested_marker = "[CONTESTED] " if "Contested" in theme else ""
    st.markdown(
        f"""
        <div class="fact-card">
        <b>Point {num}.</b> {headline}<br>
        <span style="color:#9AA5AD;">{body}</span><br>
        <span class="tag tag-interp" style="margin-top:0.4rem;">{contested_marker}{theme}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()
st.markdown(
    """
    **A note on the contested points.** Points 15 and 21 are flagged here because they go beyond a
    defence of defense-sector contracting into claims that drew significant public criticism,
    including comparisons to "technofascism" and, from a British MP, "the ramblings of a comic book
    villain." The essay treats these as a genuine internal tension in the manifesto (see the claim in
    Point 13 about advancing progressive values, sitting alongside Point 21's cultural hierarchy claim)
    rather than omitting them for a tidier argument.
    """
)
