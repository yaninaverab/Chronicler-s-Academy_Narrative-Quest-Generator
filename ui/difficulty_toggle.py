"""
difficulty_toggle.py — Per-quest difficulty override selector.

Lets the scholar pick a different difficulty for the NEXT quest only,
without changing their permanent profile preference (scholar["difficulty"]).

Usage in page_upload() and page_chronicler():
    from ui.difficulty_toggle import render_difficulty_toggle
    render_difficulty_toggle(scholar)   # call anywhere visible on the page

Then in page_generating(), read the override:
    effective_difficulty = st.session_state.get("selected_difficulty", scholar["difficulty"])
"""

import streamlit as st
from backend.translations import (
    t, translated_difficulty_options, difficulty_display_to_english,
)


def render_difficulty_toggle(scholar: dict):
    """
    Renders a compact difficulty selector.
    Defaults to the scholar's profile difficulty if no override is set yet.
    Stores the English value in st.session_state.selected_difficulty.
    """
    # Initialize override with the scholar's profile default, only once
    if "selected_difficulty" not in st.session_state:
        st.session_state.selected_difficulty = scholar.get("difficulty", "Medium")

    translated_options = translated_difficulty_options()
    difficulty_options_en = ["Easy", "Medium", "Hard"]

    current_en = st.session_state.selected_difficulty
    current_index = difficulty_options_en.index(current_en) if current_en in difficulty_options_en else 1

    col_spacer, col_toggle = st.columns([3, 2])
    with col_toggle:
        selected_display = st.select_slider(
            t("difficulty_override_label"),
            options=translated_options,
            value=translated_options[current_index],
            key="difficulty_override_widget",
        )

    selected_en = difficulty_display_to_english(selected_display)
    st.session_state.selected_difficulty = selected_en