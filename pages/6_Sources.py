import streamlit as st
from data import SOURCES
from styles import inject_base_styles, eyebrow, subtitle

st.set_page_config(page_title="Sources", page_icon="\U0001F4DA", layout="wide")
inject_base_styles()

eyebrow("EVERY CITATION USED IN THE ESSAY AND THIS SITE")
st.title("Sources")
subtitle("Course readings, primary sources, and verified news reporting")

st.markdown(
    """
    <div class="disclaimer-box">
    This list combines assigned course material (IIM Calcutta, Ethics of Technology and Its Relevance
    for Business) with externally verified sources. Course-pack readings are marked accordingly and are
    not publicly linkable; all other entries link to a live, checkable source.
    </div>
    """,
    unsafe_allow_html=True,
)

search = st.text_input("Search sources", "")

items = list(SOURCES.items())
if search:
    s = search.lower()
    items = [(k, v) for k, v in items if s in v["label"].lower() or s in v["type"].lower()]

# group by type
from collections import defaultdict
grouped = defaultdict(list)
for k, v in items:
    grouped[v["type"]].append(v)

for group_name in sorted(grouped.keys()):
    st.subheader(group_name)
    for v in grouped[group_name]:
        st.markdown(f"- {v['label']}  \n  [{v['url']}]({v['url']})")

st.divider()
st.markdown(
    """
    **Course materials cited in the essay but not listed above** (not externally linkable \u2014
    distributed via the course pack):
    - Session 15 slides, *Ethical and social concerns around military uses of technologies*
    - Sessions 5\u20136 slides, *AI Governance Frameworks*; Session 9 slides, *Values in and of Technology*; Session 18 slides, *Governance of Technologies*
    - *Google and Project Maven (A): Big Tech, Government and the AI Arms Race* \u2014 INSEAD case study
    - Feenberg, A. *What is Philosophy of Technology?*; *A Critical Theory of Technology*
    - Hagendorff, T. (2020). The ethics of AI ethics: An evaluation of guidelines. *Minds and Machines*, 30, 99\u2013120.
    - Matten, D., Crane, A., & Moon, J. *Corporate responsibility for innovation: A citizenship framework*
    """
)
