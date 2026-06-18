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


# ── CSS injected once ────────────────────────────────────────────────────────
STREAK_CSS = """
<style>
/* Streak banner */
.streak-banner {
    background: linear-gradient(135deg, #1a0a2e 0%, #2d1b4e 60%, #0d0d1a 100%);
    border: 1px solid #7b2fff;
    border-radius: 12px;
    padding: 18px 24px;
    margin: 12px 0;
    text-align: center;
    box-shadow: 0 0 18px rgba(123, 47, 255, 0.35);
}
.streak-banner h2 { color: #e8d5ff; margin: 0 0 4px 0; font-size: 1.5rem; }
.streak-banner p  { color: #a98fd4; margin: 0; font-size: 0.9rem; }

/* Milestone popup */
.milestone-popup {
    background: linear-gradient(135deg, #0d1f0d 0%, #1a3a1a 100%);
    border: 2px solid #39ff14;
    border-radius: 14px;
    padding: 22px 28px;
    text-align: center;
    box-shadow: 0 0 28px rgba(57, 255, 20, 0.4);
    animation: pulse-green 1.5s ease-in-out infinite alternate;
}
@keyframes pulse-green {
    from { box-shadow: 0 0 20px rgba(57, 255, 20, 0.3); }
    to   { box-shadow: 0 0 40px rgba(57, 255, 20, 0.7); }
}
.milestone-popup h1 { color: #39ff14; font-size: 2.5rem; margin: 0; }
.milestone-popup h3 { color: #c8ffb0; margin: 6px 0 2px 0; }
.milestone-popup p  { color: #7dff5c; margin: 0; font-size: 0.9rem; }

/* Freeze notice */
.freeze-banner {
    background: #0d1a2e;
    border: 1px solid #2255aa;
    border-radius: 10px;
    padding: 12px 18px;
    text-align: center;
    color: #88aadd;
    font-size: 0.9rem;
}

/* Compact streak badge in sidebar */
.streak-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #1a0a2e;
    border: 1px solid #5a2fa8;
    border-radius: 20px;
    padding: 6px 14px;
    color: #d0b0ff;
    font-size: 0.95rem;
    font-weight: 600;
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
    opacity: 0.4;
    transition: opacity 0.3s;
}
.milestone-node.unlocked { opacity: 1; }
.milestone-node span { display: block; font-size: 1.4rem; }
.milestone-node small { color: #a98fd4; font-size: 0.7rem; }
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
        st.markdown(f"""
        <div class="milestone-popup">
            <h1>{milestone['icon']}</h1>
            <h3>{milestone['badge']}</h3>
            <p>{milestone['title']}</p>
            <p style="margin-top:8px; color:#39ff14; font-weight:600;">
                +{milestone['bonus_xp']} XP awarded!
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state["milestone_shown"] = True

    # ── Main streak banner ───────────────────────────────────────────────
    if status == "incremented":
        subtitle = f"+{bonus_xp} XP bonus" if bonus_xp else "Keep it up, Scholar!"
        streak_label = f"Day {streak}"
    elif status == "frozen":
        subtitle = "❄️ Grace period active — log in tomorrow to keep your streak!"
        streak_label = f"Day {streak} (frozen)"
    elif status == "reset":
        subtitle = "Your streak has been reset. Begin anew, Scholar."
        streak_label = "Day 1"
    else:  # already_today
        subtitle = "You've already logged in today. Well done."
        streak_label = f"Day {streak}"

    st.markdown(f"""
    <div class="streak-banner">
        <h2>{icon} {streak_label} Streak</h2>
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
    st.markdown(
        f'<div class="streak-badge">{icon} {streak}-day streak</div>',
        unsafe_allow_html=True
    )
