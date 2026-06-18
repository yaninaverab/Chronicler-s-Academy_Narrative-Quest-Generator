"""
streak_manager.py — Daily login streak system for Chronicler's Academy
Grace period rule: miss 1 day → streak freezes. Miss 2+ days → reset to 0.
"""

from datetime import date, timedelta
from typing import Optional

# ── Milestone definitions ────────────────────────────────────────────────────
STREAK_MILESTONES = [
    {
        "days": 3,
        "icon": "🔥",
        "badge": "Ember Keeper",
        "bonus_xp": 30,
        "title": "The flame ignites…",
    },
    {
        "days": 7,
        "icon": "🔥🔥",
        "badge": "Week Warden",
        "bonus_xp": 75,
        "title": "Seven days of devotion.",
    },
    {
        "days": 14,
        "icon": "💎🔥",
        "badge": "Fortnight Forged",
        "bonus_xp": 150,
        "title": "Two weeks — the archive bows.",
    },
    {
        "days": 30,
        "icon": "👑🔥",
        "badge": "Eternal Chronicler",
        "bonus_xp": 400,
        "title": "A month unbroken. Legend.",
    },
]

def get_streak_icon(streak: int) -> str:
    """Return the highest unlocked flame icon for a given streak count."""
    icon = "⚡"  # default — no milestone yet
    for m in STREAK_MILESTONES:
        if streak >= m["days"]:
            icon = m["icon"]
    return icon

def get_milestone_for_streak(streak: int) -> Optional[dict]:
    """Return the milestone dict if today's streak count exactly hits one."""
    for m in STREAK_MILESTONES:
        if streak == m["days"]:
            return m
    return None

def compute_streak_update(
    current_streak: int,
    last_login_str: Optional[str],  # ISO date string "YYYY-MM-DD" or None
) -> dict:
    """
    Core streak logic. Returns a dict with:
      - new_streak (int)
      - status: "incremented" | "frozen" | "reset" | "already_today"
      - milestone (dict | None) — set if a milestone was just hit
      - bonus_xp (int)
    """
    today = date.today()

    # First ever login
    if last_login_str is None:
        new_streak = 1
        status = "incremented"
        milestone = get_milestone_for_streak(new_streak)
        return {
            "new_streak": new_streak,
            "status": status,
            "milestone": milestone,
            "bonus_xp": milestone["bonus_xp"] if milestone else 0,
        }

    last_login = date.fromisoformat(last_login_str)
    delta = (today - last_login).days

    if delta == 0:
        # Already logged in today — no change
        return {
            "new_streak": current_streak,
            "status": "already_today",
            "milestone": None,
            "bonus_xp": 0,
        }

    elif delta == 1:
        # Consecutive day — increment
        new_streak = current_streak + 1
        milestone = get_milestone_for_streak(new_streak)
        return {
            "new_streak": new_streak,
            "status": "incremented",
            "milestone": milestone,
            "bonus_xp": milestone["bonus_xp"] if milestone else 0,
        }

    elif delta == 2:
        # Grace period — streak freezes, no increment, no reset
        return {
            "new_streak": current_streak,
            "status": "frozen",
            "milestone": None,
            "bonus_xp": 0,
        }

    else:
        # 3+ days missed — reset
        return {
            "new_streak": 1,
            "status": "reset",
            "milestone": None,
            "bonus_xp": 0,
        }
