import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/scholars.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create all tables if they don't exist."""
    conn = get_connection()
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS scholars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pin TEXT NOT NULL,
            theme TEXT,
            difficulty TEXT,
            interests TEXT,
            play_style TEXT,
            hero_type TEXT,
            quest_style TEXT,
            reward_preference TEXT,
            total_xp INTEGER DEFAULT 0,
            rank INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS dimensions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scholar_id INTEGER NOT NULL,
            pdf_name TEXT,
            subject TEXT,
            quest_title TEXT,
            quest_json TEXT,
            score INTEGER DEFAULT 0,
            total_questions INTEGER DEFAULT 0,
            xp_earned INTEGER DEFAULT 0,
            hints_used INTEGER DEFAULT 0,
            completed INTEGER DEFAULT 0,
            completed_at TEXT,
            FOREIGN KEY (scholar_id) REFERENCES scholars(id)
        );

        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scholar_id INTEGER NOT NULL,
            dimension_id INTEGER,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (scholar_id) REFERENCES scholars(id)
        );
    """)

    conn.commit()
    conn.close()

# ── Scholar functions ─────────────────────────────────────────

def create_scholar(name, pin, theme, difficulty, interests,
                   play_style="", hero_type="",
                   quest_style="", reward_preference=""):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO scholars 
        (name, pin, theme, difficulty, interests, 
         play_style, hero_type, quest_style, reward_preference)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, pin, theme, difficulty, interests,
          play_style, hero_type, quest_style, reward_preference))
    conn.commit()
    scholar_id = c.lastrowid
    conn.close()
    return scholar_id

def get_scholar(name, pin):
    """Returns scholar if name+pin match, None otherwise."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT id, name, pin, theme, difficulty, interests,
               play_style, hero_type, quest_style, reward_preference,
               total_xp, rank, created_at,
               current_streak, longest_streak, last_login_date, streak_badges
        FROM scholars
        WHERE name=? AND pin=?
    """, (name, pin))
    row = c.fetchone()
    if not row:
        return None
    scholar = dict(row)
    scholar["xp"] = scholar["total_xp"]  # alias for streak system compatibility
    return scholar

def name_exists(name):
    """Check if a scholar name is already taken."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM scholars WHERE name=?", (name,))
    row = c.fetchone()
    conn.close()
    return row is not None

def add_xp(scholar_id, xp_amount):
    """Add XP and update rank automatically."""
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT total_xp FROM scholars WHERE id=?", (scholar_id,))
    row = c.fetchone()
    new_xp = row["total_xp"] + xp_amount

    # Calculate rank from new XP
    new_rank = calculate_rank(new_xp)

    c.execute("""
        UPDATE scholars SET total_xp=?, rank=? WHERE id=?
    """, (new_xp, new_rank, scholar_id))
    conn.commit()
    conn.close()
    return new_xp, new_rank

def calculate_rank(xp):
    if xp >= 2000:
        return 5
    elif xp >= 1000:
        return 4
    elif xp >= 500:
        return 3
    elif xp >= 200:
        return 2
    return 1

def get_rank_info(rank):
    ranks = {
        1: {"title": "Apprentice Chrono-Scholar", "emoji": "📜"},
        2: {"title": "Adept Chrono-Scholar",      "emoji": "⚗️"},
        3: {"title": "Dimensional Seeker",         "emoji": "🌀"},
        4: {"title": "Master of Realms",           "emoji": "🔮"},
        5: {"title": "Chrono-Legend",              "emoji": "⚡"},
    }
    return ranks.get(rank, ranks[1])

def get_xp_for_next_rank(rank):
    thresholds = {1: 200, 2: 500, 3: 1000, 4: 2000, 5: None}
    return thresholds.get(rank)

# ── Dimension functions ───────────────────────────────────────

def create_dimension(scholar_id, pdf_name, subject, quest_title, quest_json):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO dimensions
        (scholar_id, pdf_name, subject, quest_title, quest_json)
        VALUES (?, ?, ?, ?, ?)
    """, (scholar_id, pdf_name, subject, quest_title,
          json.dumps(quest_json)))
    conn.commit()
    dim_id = c.lastrowid
    conn.close()
    return dim_id

def complete_dimension(dimension_id, score, total_questions,
                       xp_earned, hints_used):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        UPDATE dimensions
        SET score=?, total_questions=?, xp_earned=?,
            hints_used=?, completed=1, completed_at=?
        WHERE id=?
    """, (score, total_questions, xp_earned,
          hints_used, datetime.now().isoformat(), dimension_id))
    conn.commit()
    conn.close()

def get_scholar_dimensions(scholar_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM dimensions
        WHERE scholar_id=? AND completed=1
        ORDER BY completed_at DESC
    """, (scholar_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

# ── Chat history functions ────────────────────────────────────

def save_message(scholar_id, role, message, dimension_id=None):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO chat_history
        (scholar_id, dimension_id, role, message)
        VALUES (?, ?, ?, ?)
    """, (scholar_id, dimension_id, role, message))
    conn.commit()
    conn.close()

def get_chat_history(scholar_id, dimension_id=None):
    conn = get_connection()
    c = conn.cursor()
    if dimension_id:
        c.execute("""
            SELECT role, message FROM chat_history
            WHERE scholar_id=? AND dimension_id=?
            ORDER BY created_at ASC
        """, (scholar_id, dimension_id))
    else:
        c.execute("""
            SELECT role, message FROM chat_history
            WHERE scholar_id=?
            ORDER BY created_at DESC LIMIT 20
        """, (scholar_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]