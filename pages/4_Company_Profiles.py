import streamlit as st
from data import PROFILES, INK, GREY
from styles import inject_base_styles, eyebrow, subtitle, quote_box, tag

st.set_page_config(page_title="Company Profiles", page_icon="\U0001F3E2", layout="wide")
inject_base_styles()

eyebrow("SECTIONS 2\u20134 OF THE ESSAY \u2014 COMPANY DEEP-DIVES")
st.title("Company Profiles")
subtitle("Key facts, primary-source quotes, and the essay's reading of each firm")

st.markdown(
    """
    <div class="disclaimer-box">
    Each tab separates <span class="tag tag-fact">VERIFIED FACT</span> (dated, sourced events) from
    <span class="tag tag-interp">OUR INTERPRETATION</span> (the essay's own analytical argument about
    what those facts mean). The quote in each profile is a direct primary-source statement.
    </div>
    """,
    unsafe_allow_html=True,
)

tabs = st.tabs(list(PROFILES.keys()))

for tab, (company, profile) in zip(tabs, PROFILES.items()):
    with tab:
        st.markdown(f"### {company}")
        st.markdown(f"**Narrative:** :orange[{profile['narrative']}]")
        st.write(profile["summary"])

        quote_box(profile["key_quote"][0], profile["key_quote"][1])

        col1, col2 = st.columns([1, 1])
        with col1:
            tag("fact")
            st.markdown("#### Key Facts")
            for date, fact in profile["facts"]:
                st.markdown(
                    f"""
                    <div class="fact-card">
                    <span class="fact-date">{date}</span><br>{fact}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        with col2:
            tag("interp")
            st.markdown("#### The Essay's Reading")
            st.markdown(
                f"""
                <div class="fact-card" style="border-left-color:#8A6D22;">
                {profile['our_reading']}
                </div>
                """,
                unsafe_allow_html=True,
            )

st.divider()
st.caption("For full sourcing on every claim above, see the Sources page.")
