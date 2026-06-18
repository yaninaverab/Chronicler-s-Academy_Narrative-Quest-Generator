"""
theme.py — Dark RPG visual theme for Chronicler's Academy.
Inject this CSS into every Streamlit page via inject_theme().

Usage:
    from ui.theme import inject_theme, rpg_card, xp_bar, stat_pill, page_header
    inject_theme()   # call once at top of every page function
"""

import streamlit as st

# ── Google Fonts ──────────────────────────────────────────────────────────────
FONTS_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
"""

# ── Master CSS ────────────────────────────────────────────────────────────────
THEME_CSS = """
<style>
/* ── Tokens ──────────────────────────────────────────────────────────── */
:root {
    --void:        #0a0812;
    --void-2:      #100d1c;
    --void-3:      #1a1530;
    --parchment:   #e8d5b0;
    --parchment-2: #c4aa7a;
    --parchment-3: #8a7050;
    --arcane:      #7b2fff;
    --arcane-dim:  #4a1fa8;
    --arcane-glow: rgba(123,47,255,0.25);
    --gold:        #c9a84c;
    --gold-dim:    #7a5f1a;
    --gold-glow:   rgba(201,168,76,0.2);
    --ember:       #c0392b;
    --ember-dim:   #7a1f15;
    --ghost:       rgba(232,213,176,0.07);
    --border:      rgba(123,47,255,0.3);
    --border-gold: rgba(201,168,76,0.35);
    --font-display: 'Cinzel', serif;
    --font-body:    'Inter', sans-serif;
    --font-mono:    'JetBrains Mono', monospace;
    --radius:       10px;
    --radius-lg:    16px;
}

/* ── Global overrides ────────────────────────────────────────────────── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: var(--void) !important;
    color: var(--parchment) !important;
    font-family: var(--font-body) !important;
}
[data-testid="stSidebar"] {
    background-color: var(--void-2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--parchment) !important; }

/* ── Hide Streamlit chrome ───────────────────────────────────────────── */
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stToolbar"] { display: none !important; }

/* ── Typography ──────────────────────────────────────────────────────── */
h1, h2, h3 {
    font-family: var(--font-display) !important;
    color: var(--gold) !important;
    letter-spacing: 0.04em;
}
h1 { font-size: 2.2rem !important; font-weight: 700 !important; }
h2 { font-size: 1.5rem !important; font-weight: 600 !important; }
h3 { font-size: 1.1rem !important; font-weight: 600 !important; }
p, li, span, label { font-family: var(--font-body) !important; color: var(--parchment) !important; }
code, pre { font-family: var(--font-mono) !important; color: var(--arcane) !important; }

/* ── Inputs ──────────────────────────────────────────────────────────── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input {
    background-color: var(--void-3) !important;
    border: 1px solid var(--border) !important;
    color: var(--parchment) !important;
    font-family: var(--font-body) !important;
    border-radius: var(--radius) !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--arcane) !important;
    box-shadow: 0 0 0 2px var(--arcane-glow) !important;
}

/* ── Buttons ─────────────────────────────────────────────────────────── */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, var(--arcane-dim), var(--arcane)) !important;
    border: 1px solid var(--arcane) !important;
    color: var(--parchment) !important;
    font-family: var(--font-display) !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.06em !important;
    border-radius: var(--radius) !important;
    transition: all 0.2s ease !important;
    padding: 0.5rem 1.4rem !important;
}
[data-testid="stButton"] button:hover {
    background: linear-gradient(135deg, var(--arcane), #9b4fff) !important;
    box-shadow: 0 0 14px var(--arcane-glow) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid var(--border-gold) !important;
    color: var(--gold) !important;
}
[data-testid="stButton"] button[kind="secondary"]:hover {
    background: var(--gold-glow) !important;
    box-shadow: 0 0 10px var(--gold-glow) !important;
}

/* ── Select / Radio ──────────────────────────────────────────────────── */
[data-testid="stSelectbox"] select,
[data-testid="stRadio"] label {
    color: var(--parchment) !important;
    font-family: var(--font-body) !important;
}
[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {
    color: var(--parchment) !important;
}

/* ── Tabs ────────────────────────────────────────────────────────────── */
[data-testid="stTabs"] [role="tablist"] {
    border-bottom: 1px solid var(--border) !important;
}
[data-testid="stTabs"] [role="tab"] {
    color: var(--parchment-3) !important;
    font-family: var(--font-display) !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.05em !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: var(--gold) !important;
    border-bottom: 2px solid var(--gold) !important;
}

/* ── Metrics ─────────────────────────────────────────────────────────── */
[data-testid="stMetric"] {
    background: var(--void-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1rem !important;
}
[data-testid="stMetricLabel"] { color: var(--parchment-3) !important; font-size: 0.8rem !important; }
[data-testid="stMetricValue"] { color: var(--gold) !important; font-family: var(--font-display) !important; }

/* ── Divider ─────────────────────────────────────────────────────────── */
hr {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 1.5rem 0 !important;
}

/* ── Scrollbar ───────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--void); }
::-webkit-scrollbar-thumb { background: var(--arcane-dim); border-radius: 3px; }

/* ── Expander ────────────────────────────────────────────────────────── */
[data-testid="stExpander"] {
    background: var(--void-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}
[data-testid="stExpander"] summary {
    color: var(--parchment) !important;
    font-family: var(--font-display) !important;
    font-size: 0.85rem !important;
}
</style>
"""

# ── Component HTML builders ───────────────────────────────────────────────────

def inject_theme():
    """Call once at the top of every page function."""
    st.markdown(FONTS_HTML, unsafe_allow_html=True)
    st.markdown(THEME_CSS, unsafe_allow_html=True)


def page_header(title: str, subtitle: str = "", icon: str = "📜"):
    """Dramatic page header in Cinzel with rune divider."""
    subtitle_html = "" if not subtitle else f'<p style="color:#8a7050; font-size:0.9rem; margin-top:0.4rem; letter-spacing:0.04em;">{subtitle}</p>'
    st.markdown(f"""
    <div style="text-align:center; padding: 2rem 0 1rem;">
        <div style="font-size:2.8rem; margin-bottom:0.4rem;">{icon}</div>
        <h1 style="font-family:'Cinzel',serif; color:#c9a84c; font-size:2rem; letter-spacing:0.08em; margin:0;">{title}</h1>
        {subtitle_html}
        <div style="margin:1rem auto 0; width:200px; height:1px; background:linear-gradient(90deg,transparent,#c9a84c,transparent);"></div>
    </div>
    """, unsafe_allow_html=True)

def rpg_card(title: str, body: str, accent: str = "arcane", footer: str = ""):
    """
    A bordered RPG-style card.
    accent: "arcane" (purple) | "gold" | "ember" (red/danger)
    """
    colors = {
        "arcane": ("rgba(123,47,255,0.3)", "#7b2fff"),
        "gold":   ("rgba(201,168,76,0.3)",  "#c9a84c"),
        "ember":  ("rgba(192,57,43,0.3)",   "#c0392b"),
    }
    border_color, glow_color = colors.get(accent, colors["arcane"])

    footer_html = f'<div style="margin-top:12px;padding-top:10px;border-top:1px solid {border_color};color:#8a7050;font-size:0.78rem;">{footer}</div>' if footer else ""

    card_html = '<div style="background:#100d1c;border:1px solid ' + border_color + ';border-radius:12px;padding:1.2rem 1.4rem;margin:0.6rem 0;position:relative;box-shadow:inset 0 0 30px rgba(0,0,0,0.4);">' + \
        f'<div style="position:absolute; top:-1px; left:20px; right:20px; height:1px; background:linear-gradient(90deg,transparent,{glow_color},transparent);"></div>' + \
        '<h3 style="font-family:\'Cinzel\',serif;color:#c9a84c;font-size:0.95rem;letter-spacing:0.06em;margin:0 0 8px;">' + title + '</h3>' + \
        '<div style="color:#e8d5b0;font-size:0.9rem;line-height:1.6;">' + body + '</div>' + \
        footer_html + \
        f'<div style="position:absolute; bottom:-1px; left:20px; right:20px; height:1px; background:linear-gradient(90deg,transparent,{glow_color},transparent);"></div>' + \
        '</div>'

    st.markdown(card_html, unsafe_allow_html=True)


def xp_bar(current_xp: int, next_threshold: int, rank_title: str, rank_num: int):
    """Animated XP progress bar styled as a potion/mana vial."""
    pct = min(100, int((current_xp / max(next_threshold, 1)) * 100))
    remaining = next_threshold - current_xp

    st.markdown(f"""
    <div style="margin: 0.8rem 0;">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:6px;">
            <span style="font-family:'Cinzel',serif; color:#c9a84c; font-size:0.8rem; letter-spacing:0.05em;">
                ✦ {rank_title}
            </span>
            <span style="font-family:'JetBrains Mono',monospace; color:#8a7050; font-size:0.75rem;">
                {current_xp} / {next_threshold} XP
            </span>
        </div>
        <div style="
            background: #1a1530;
            border: 1px solid rgba(123,47,255,0.4);
            border-radius: 20px;
            height: 10px;
            overflow: hidden;
            position: relative;
        ">
            <div style="
                width: {pct}%;
                height: 100%;
                background: linear-gradient(90deg, #4a1fa8, #7b2fff, #9b5fff);
                border-radius: 20px;
                transition: width 0.8s ease;
                box-shadow: 0 0 8px rgba(123,47,255,0.6);
            "></div>
        </div>
        <div style="text-align:right; margin-top:4px;
                    font-size:0.72rem; color:#8a7050; font-family:'JetBrains Mono',monospace;">
            {remaining} XP to next rank
        </div>
    </div>
    """, unsafe_allow_html=True)


def stat_pill(label: str, value: str, color: str = "arcane"):
    """Inline stat pill — use in a st.columns layout."""
    colors = {
        "arcane": ("#1a0a2e", "#7b2fff", "#d0b0ff"),
        "gold":   ("#1a1200", "#c9a84c", "#f5e199"),
        "ember":  ("#1a0500", "#c0392b", "#ffb0a8"),
        "teal":   ("#001a15", "#1abc9c", "#a0ffe8"),
    }
    bg, border, text = colors.get(color, colors["arcane"])

    st.markdown(f"""
    <div style="
        background:{bg}; border:1px solid {border};
        border-radius:20px; padding:6px 14px;
        text-align:center; margin:4px 0;
    ">
        <div style="color:{border}; font-size:0.65rem;
                    font-family:'Cinzel',serif; letter-spacing:0.08em; text-transform:uppercase;">
            {label}
        </div>
        <div style="color:{text}; font-family:'JetBrains Mono',monospace;
                    font-size:1rem; font-weight:500; margin-top:2px;">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)


def quest_scroll(title: str, topic: str, difficulty: str, num_questions: int):
    """
    A sealed scroll card for the quest intro page.
    """
    diff_config = {
        "easy":      ("⚗️", "#1abc9c", "Apprentice"),
        "medium":    ("🔮", "#7b2fff", "Seeker"),
        "hard":      ("⚔️", "#c9a84c", "Master"),
        "legendary": ("👑", "#c0392b", "Chrono-Legend"),
    }
    icon, color, label = diff_config.get(difficulty, diff_config["medium"])

    st.markdown(f"""
    <div style="
        background: #0d0a1a;
        border: 1px solid {color}55;
        border-radius: 14px;
        padding: 2rem;
        text-align: center;
        position: relative;
        margin: 1rem 0;
    ">
        <div style="
            position:absolute; top:0; left:0; right:0;
            height:3px; border-radius:14px 14px 0 0;
            background:linear-gradient(90deg, transparent, {color}, transparent);
        "></div>
        <div style="font-size:2.5rem; margin-bottom:0.5rem;">{icon}</div>
        <div style="
            font-family:'Cinzel',serif; color:#c9a84c;
            font-size:1.3rem; font-weight:700; letter-spacing:0.06em;
            margin-bottom:0.3rem;
        ">{title}</div>
        <div style="color:#8a7050; font-size:0.85rem; margin-bottom:1.2rem;">{topic}</div>
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
            <span style="
                background:{color}22; border:1px solid {color}55;
                color:{color}; border-radius:20px;
                padding:4px 14px; font-size:0.78rem;
                font-family:'Cinzel',serif; letter-spacing:0.05em;
            ">{label}</span>
            <span style="
                background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.3);
                color:#c9a84c; border-radius:20px;
                padding:4px 14px; font-size:0.78rem;
                font-family:'JetBrains Mono',monospace;
            ">{num_questions} Challenges</span>
        </div>
        <div style="
            position:absolute; bottom:0; left:0; right:0;
            height:3px; border-radius:0 0 14px 14px;
            background:linear-gradient(90deg, transparent, {color}, transparent);
        "></div>
    </div>
    """, unsafe_allow_html=True)


def notification_toast(message: str, kind: str = "info"):
    """
    Floating notification banner.
    kind: "info" | "success" | "warning" | "danger"
    """
    config = {
        "info":    ("#1a1530", "#7b2fff", "📜"),
        "success": ("#0d1a10", "#1abc9c", "✦"),
        "warning": ("#1a1200", "#c9a84c", "⚠"),
        "danger":  ("#1a0505", "#c0392b", "✕"),
    }
    bg, border, icon = config.get(kind, config["info"])
    st.markdown(f"""
    <div style="
        background:{bg}; border:1px solid {border}55;
        border-left:3px solid {border};
        border-radius:8px; padding:12px 16px;
        display:flex; align-items:center; gap:10px;
        margin:8px 0; color:#e8d5b0; font-size:0.88rem;
    ">
        <span style="color:{border}; font-size:1rem;">{icon}</span>
        {message}
    </div>
    """, unsafe_allow_html=True)
