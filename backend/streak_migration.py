"""
streak_migration.py — Adds streak columns to the existing scholars table.
Run this ONCE, or call apply_streak_migration() safely on every startup
(it checks if columns already exist before altering).
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/scholars.db")


def apply_streak_migration(db_path: str = DB_PATH):
    """
    Safely adds streak columns to the scholars table if they don't exist yet.
    Idempotent — safe to call on every app startup.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch existing column names
    cursor.execute("PRAGMA table_info(scholars)")
    existing_columns = {row[1] for row in cursor.fetchall()}

    migrations = [
        ("current_streak",  "INTEGER DEFAULT 0"),
        ("longest_streak",  "INTEGER DEFAULT 0"),
        ("last_login_date", "TEXT DEFAULT NULL"),
        ("streak_badges",   "TEXT DEFAULT ''"),   # comma-separated badge names
    ]

    for col_name, col_def in migrations:
        if col_name not in existing_columns:
            cursor.execute(
                f"ALTER TABLE scholars ADD COLUMN {col_name} {col_def}"
            )
            print(f"[streak_migration] Added column: {col_name}")
        else:
            print(f"[streak_migration] Column already exists: {col_name}")

    conn.commit()
    conn.close()
    print("[streak_migration] Migration complete.")


def update_scholar_streak(
    db_path: str,
    scholar_id: int,
    new_streak: int,
    last_login_date: str,   # ISO "YYYY-MM-DD"
    bonus_xp: int,
    new_badge: str = "",    # badge name to append, or ""
):
    """
    Persists streak update results to the database.
    - Updates current_streak, longest_streak, last_login_date
    - Adds bonus_xp to total xp
    - Appends new badge if earned
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch current longest streak and existing badges
    cursor.execute(
        "SELECT longest_streak, streak_badges, total_xp FROM scholars WHERE id = ?",
        (scholar_id,)
    )
    row = cursor.fetchone()
    if not row:
        conn.close()
        return

    longest, badges_str, current_xp = row
    new_longest = max(longest or 0, new_streak)

    # Append badge if earned and not already collected
    existing_badges = [b for b in (badges_str or "").split(",") if b]
    if new_badge and new_badge not in existing_badges:
        existing_badges.append(new_badge)
    updated_badges = ",".join(existing_badges)

    cursor.execute(
        """
        UPDATE scholars
        SET current_streak  = ?,
            longest_streak  = ?,
            last_login_date = ?,
            streak_badges   = ?,
            total_xp        = total_xp + ?
        WHERE id = ?
        """,
        (new_streak, new_longest, last_login_date, updated_badges, bonus_xp, scholar_id)
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    apply_streak_migration()
