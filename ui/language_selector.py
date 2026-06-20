"""
language_selector.py — Top-right language toggle for the login page.

Usage in app.py's page_login():
    from ui.language_selector import render_language_selector
    render_language_selector()  # call at the very top of page_login()
"""

import streamlit as st

LANGUAGE_SELECTOR_CSS = """<style>
div[data-testid="stSelectbox"] {
margin-top: 0.3rem;
}
div[data-testid="stSelectbox"] > div > div {
background-color: #0d0a1a !important;
border: 1px solid rgba(123,47,255,0.4) !important;
border-radius: 20px !important;
color: #e8d5b0 !important;
font-family: 'Cinzel', serif !important;
font-size: 0.78rem !important;
}
div[data-testid="stSelectbox"] > div > div:hover {
border-color: #7b2fff !important;
box-shadow: 0 0 8px rgba(123,47,255,0.3) !important;
}
</style>"""


def render_language_selector():
    """
    Renders a small language selector in the top-right corner,
    styled to match the dark arcane theme.
    Sets st.session_state.language to "es" or "en".
    Defaults to "es" if not yet set.
    """
    if "language" not in st.session_state:
        st.session_state.language = "es"

    st.markdown(LANGUAGE_SELECTOR_CSS, unsafe_allow_html=True)

    # Push the selector to the top-right using columns
    col_spacer, col_selector = st.columns([5, 1])

    with col_selector:
        options = {"🇪🇸 ES": "es", "🇬🇧 EN": "en"}
        labels = list(options.keys())
        current_lang = st.session_state.language
        current_label = "🇪🇸 ES" if current_lang == "es" else "🇬🇧 EN"
        current_index = labels.index(current_label)

        selected_label = st.selectbox(
            "🌐",
            labels,
            index=current_index,
            key="language_selector_widget",
            label_visibility="collapsed",
        )

        selected_lang = options[selected_label]
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()
