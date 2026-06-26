"""
streak_ui.py — Streamlit UI components for the streak system.
Drop these calls into app.py at the right moments:
  - handle_login_streak()  → call right after successful login
  - render_streak_panel()  → call in the academy home sidebar/header
"""

import streamlit as st
from datetime import date
from backend.streak_manager import compute_streak_update, get_streak_icon, STREAK_MILESTONES
from backend.streak_migration import update_scholar_streak, DB_PATH
from backend.translations import t


# ── CSS injected once ────────────────────────────────────────────────────────
STREAK_CSS = """
<style>
@keyframes streak-pulse {
    0%, 100% { box-shadow: 0 0 15px rgba(123,47,255,0.3); }
    50%       { box-shadow: 0 0 35px rgba(123,47,255,0.65), 0 0 60px rgba(123,47,255,0.15); }
}
@keyframes milestone-glow {
    from { box-shadow: 0 0 20px rgba(26,188,156,0.35); }
    to   { box-shadow: 0 0 45px rgba(26,188,156,0.75), 0 0 80px rgba(26,188,156,0.2); }
}

/* Streak banner */
.streak-banner {
    background: linear-gradient(135deg, #05030f 0%, #0f0c22 50%, #08051a 100%);
    border: 1px solid rgba(123,47,255,0.35);
    border-radius: 14px;
    padding: 16px 22px;
    margin: 10px 0;
    text-align: center;
    animation: streak-pulse 3s ease-in-out infinite;
    position: relative;
    overflow: hidden;
}
.streak-banner::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(123,47,255,0.6), transparent);
}
.streak-banner h2 {
    color: #c8a8ff;
    margin: 0 0 4px 0;
    font-size: 1.35rem;
    font-family: 'Cinzel', serif;
    letter-spacing: 0.06em;
}
.streak-banner p { color: #7b5fa8; margin: 0; font-size: 0.82rem; }

/* Milestone popup */
.milestone-popup {
    background: linear-gradient(135deg, #030f08 0%, #081a10 100%);
    border: 2px solid rgba(26,188,156,0.6);
    border-radius: 16px;
    padding: 22px 28px;
    text-align: center;
    animation: milestone-glow 1.5s ease-in-out infinite alternate;
    position: relative;
    overflow: hidden;
}
.milestone-popup::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, #1abc9c, transparent);
}
.milestone-popup h1 { color: #1abc9c; font-size: 2.5rem; margin: 0; }
.milestone-popup h3 { color: #a0ffe8; margin: 6px 0 2px 0; font-family: 'Cinzel', serif; }
.milestone-popup p  { color: #5dffd8; margin: 0; font-size: 0.85rem; }

/* Freeze notice */
.freeze-banner {
    background: #030814;
    border: 1px solid rgba(34,85,170,0.4);
    border-radius: 10px;
    padding: 12px 18px;
    text-align: center;
    color: #6688cc;
    font-size: 0.85rem;
}

/* Compact streak badge in sidebar */
.streak-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #0a0618, #0f0c22);
    border: 1px solid rgba(123,47,255,0.35);
    border-radius: 20px;
    padding: 6px 14px;
    color: #c8a8ff;
    font-size: 0.88rem;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
}

/* Milestone road */
.milestone-road {
    display: flex;
    justify-content: space-around;
    margin: 14px 0;
    flex-wrap: wrap;
    gap: 8px;
}
.milestone-node {
    text-align: center;
    opacity: 0.25;
    transition: opacity 0.4s, transform 0.3s;
}
.milestone-node.unlocked { opacity: 1; transform: scale(1.05); }
.milestone-node span { display: block; font-size: 1.3rem; }
.milestone-node small {
    color: #5a3a8a;
    font-size: 0.65rem;
    font-family: 'Cinzel', serif;
    letter-spacing: 0.05em;
}
</style>
"""


def inject_streak_css():
    st.markdown(STREAK_CSS, unsafe_allow_html=True)


# ── Core handler — call right after login ────────────────────────────────────
def handle_login_streak(scholar: dict, db_path: str = DB_PATH):
    """
    Call this once per session, right after the scholar logs in.
    scholar dict must have: id, current_streak, last_login_date

    Stores result in st.session_state["streak_result"] so the
    academy page can display it without re-running DB logic.
    """
    if st.session_state.get("streak_handled"):
        return  # Already processed this session

    result = compute_streak_update(
        current_streak=scholar.get("current_streak", 0),
        last_login_str=scholar.get("last_login_date"),
    )

    today_str = date.today().isoformat()
    new_badge = result["milestone"]["badge"] if result["milestone"] else ""

    if result["status"] != "already_today":
        update_scholar_streak(
            db_path=db_path,
            scholar_id=scholar["id"],
            new_streak=result["new_streak"],
            last_login_date=today_str,
            bonus_xp=result["bonus_xp"],
            new_badge=new_badge,
        )

    st.session_state["streak_result"] = result
    st.session_state["streak_handled"] = True


# ── Academy home: full streak panel ─────────────────────────────────────────
def render_streak_panel(scholar: dict):
    """
    Full streak widget for the academy home page.
    Reads st.session_state["streak_result"] set by handle_login_streak().
    """
    inject_streak_css()

    result = st.session_state.get("streak_result", {})
    streak = result.get("new_streak", scholar.get("current_streak", 0))
    status = result.get("status", "already_today")
    milestone = result.get("milestone")
    bonus_xp = result.get("bonus_xp", 0)
    icon = get_streak_icon(streak)

    # ── Milestone popup (shown once per session) ─────────────────────────
    if milestone and not st.session_state.get("milestone_shown"):
        xp_awarded_text = t("streak_milestone_xp", xp=milestone["bonus_xp"])
        st.markdown(f"""
        <div class="milestone-popup">
            <h1>{milestone['icon']}</h1>
            <h3>{milestone['badge']}</h3>
            <p>{milestone['title']}</p>
            <p style="margin-top:8px; color:#39ff14; font-weight:600;">
                {xp_awarded_text}
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state["milestone_shown"] = True

    # ── Main streak banner ───────────────────────────────────────────────
    if status == "incremented":
        subtitle = t("streak_bonus_xp", xp=bonus_xp) if bonus_xp else t("streak_keep_going")
        streak_label = t("streak_day_count", day=streak)
    elif status == "frozen":
        subtitle = t("streak_frozen_notice")
        streak_label = t("streak_day_frozen", day=streak)
    elif status == "reset":
        subtitle = t("streak_reset_notice")
        streak_label = t("streak_day_count", day=1)
    else:  # already_today
        subtitle = t("streak_already_today")
        streak_label = t("streak_day_count", day=streak)

    st.markdown(f"""
    <div class="streak-banner">
        <h2>{icon} {streak_label}</h2>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Milestone road ───────────────────────────────────────────────────
    node_parts = []
    for m in STREAK_MILESTONES:
        unlocked_class = "milestone-node unlocked" if streak >= m["days"] else "milestone-node"
        node_html = (
            f'<div class="{unlocked_class}">'
            f'<span>{m["icon"]}</span>'
            f'<small>{m["days"]}d<br>{m["badge"]}</small>'
            f'</div>'
        )
        node_parts.append(node_html)

    road_html = '<div class="milestone-road">' + "".join(node_parts) + '</div>'
    st.markdown(road_html, unsafe_allow_html=True)


# ── Sidebar: compact streak badge ────────────────────────────────────────────
def render_streak_badge(scholar: dict):
    """
    Tiny inline badge for the sidebar — shows current streak + icon.
    """
    inject_streak_css()
    streak = scholar.get("current_streak", 0)
    icon = get_streak_icon(streak)
    day_word = "día" if streak == 1 else "días"
    badge_text = f"{icon} {streak} {day_word} de racha"
    st.markdown(f'<div class="streak-badge">{badge_text}</div>', 
        unsafe_allow_html=True
    )