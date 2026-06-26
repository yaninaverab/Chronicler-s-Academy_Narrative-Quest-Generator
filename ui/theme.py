"""
theme.py — Dark RPG visual theme for Chronicler's Academy.
"""

import streamlit as st

# ── Google Fonts ──────────────────────────────────────────────────────────────
FONTS_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cinzel+Decorative:wght@400;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
"""

# ── Master CSS Part 1: Tokens + Global ───────────────────────────────────────
THEME_CSS_1 = """
<style>
:root {
    --void:        #05030f;
    --void-2:      #0d0a1f;
    --void-3:      #160f2e;
    --void-4:      #1e1640;
    --parchment:   #e8d5b0;
    --parchment-2: #c4aa7a;
    --parchment-3: #8a7050;
    --parchment-4: #5a4830;
    --arcane:      #7b2fff;
    --arcane-2:    #9b4fff;
    --arcane-dim:  #3d1880;
    --arcane-glow: rgba(123,47,255,0.3);
    --arcane-glow-strong: rgba(123,47,255,0.55);
    --gold:        #c9a84c;
    --gold-2:      #e8c96a;
    --gold-dim:    #6b4e10;
    --gold-glow:   rgba(201,168,76,0.25);
    --ember:       #c0392b;
    --ember-dim:   #6b1a12;
    --teal:        #1abc9c;
    --teal-dim:    #0d6b52;
    --ghost:       rgba(232,213,176,0.06);
    --border:      rgba(123,47,255,0.28);
    --border-gold: rgba(201,168,76,0.32);
    --border-teal: rgba(26,188,156,0.3);
    --font-display: 'Cinzel', serif;
    --font-decorative: 'Cinzel Decorative', serif;
    --font-body:    'Inter', sans-serif;
    --font-mono:    'JetBrains Mono', monospace;
    --radius:       10px;
    --radius-lg:    16px;
    --radius-xl:    24px;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: var(--void) !important;
    color: var(--parchment) !important;
    font-family: var(--font-body) !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--void-2) 0%, var(--void) 100%) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--parchment) !important; }
[data-testid="stSidebar"] hr { border-color: var(--border) !important; }

#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
</style>
"""

# ── Master CSS Part 2: Typography + Inputs ────────────────────────────────────
THEME_CSS_2 = """
<style>
h1, h2, h3 {
    font-family: var(--font-display) !important;
    color: var(--gold) !important;
    letter-spacing: 0.04em;
}
h1 { font-size: 2.2rem !important; font-weight: 700 !important; }
h2 { font-size: 1.5rem !important; font-weight: 600 !important; }
h3 { font-size: 1.1rem !important; font-weight: 600 !important; }
p, li, span, label { font-family: var(--font-body) !important; color: var(--parchment) !important; }
code, pre { font-family: var(--font-mono) !important; color: var(--arcane-2) !important; }

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input {
    background-color: var(--void-3) !important;
    border: 1px solid var(--border) !important;
    color: var(--parchment) !important;
    font-family: var(--font-body) !important;
    border-radius: var(--radius) !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--arcane) !important;
    box-shadow: 0 0 0 2px var(--arcane-glow), 0 0 20px var(--arcane-glow) !important;
}
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label {
    color: var(--parchment-3) !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.04em !important;
    font-family: var(--font-display) !important;
}

[data-testid="stButton"] button {
    background: linear-gradient(135deg, var(--arcane-dim), var(--arcane)) !important;
    border: 1px solid var(--arcane) !important;
    color: var(--parchment) !important;
    font-family: var(--font-display) !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.08em !important;
    border-radius: var(--radius) !important;
    transition: all 0.25s ease !important;
    padding: 0.55rem 1.5rem !important;
    text-transform: uppercase !important;
    position: relative !important;
    overflow: hidden !important;
}
[data-testid="stButton"] button::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    transition: left 0.4s ease;
}
[data-testid="stButton"] button:hover::before { left: 100%; }
[data-testid="stButton"] button:hover {
    background: linear-gradient(135deg, var(--arcane), var(--arcane-2)) !important;
    box-shadow: 0 0 20px var(--arcane-glow-strong), 0 4px 15px rgba(0,0,0,0.4) !important;
    transform: translateY(-2px) !important;
}
[data-testid="stButton"] button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid var(--border-gold) !important;
    color: var(--gold) !important;
}
[data-testid="stButton"] button[kind="secondary"]:hover {
    background: var(--gold-glow) !important;
    box-shadow: 0 0 14px var(--gold-glow) !important;
    transform: translateY(-1px) !important;
}
</style>
"""

# ── Master CSS Part 3: Controls + Misc ────────────────────────────────────────
THEME_CSS_3 = """
<style>
[data-testid="stSelectbox"] > div > div {
    background-color: var(--void-3) !important;
    border: 1px solid var(--border) !important;
    color: var(--parchment) !important;
    border-radius: var(--radius) !important;
}
[data-testid="stSelectbox"] label {
    color: var(--parchment-3) !important;
    font-family: var(--font-display) !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.04em !important;
}
[data-testid="stRadio"] label { color: var(--parchment) !important; font-family: var(--font-body) !important; }
[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p { color: var(--parchment) !important; }
[data-testid="stRadio"] > label { font-family: var(--font-display) !important; font-size: 0.82rem !important; letter-spacing: 0.04em !important; color: var(--parchment-3) !important; }
[data-testid="stCheckbox"] label { color: var(--parchment) !important; }
[data-testid="stSlider"] [data-testid="stMarkdownContainer"] p { color: var(--parchment-3) !important; }

[data-testid="stTabs"] [role="tablist"] { border-bottom: 1px solid var(--border) !important; background: transparent !important; }
[data-testid="stTabs"] [role="tab"] { color: var(--parchment-3) !important; font-family: var(--font-display) !important; font-size: 0.78rem !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; padding: 0.6rem 1.2rem !important; transition: color 0.2s !important; }
[data-testid="stTabs"] [role="tab"][aria-selected="true"] { color: var(--gold) !important; border-bottom: 2px solid var(--gold) !important; }
[data-testid="stTabs"] [role="tab"]:hover { color: var(--parchment) !important; }

[data-testid="stMetric"] { background: var(--void-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius) !important; padding: 1rem !important; }
[data-testid="stMetricLabel"] { color: var(--parchment-3) !important; font-size: 0.78rem !important; font-family: var(--font-display) !important; letter-spacing: 0.05em !important; }
[data-testid="stMetricValue"] { color: var(--gold) !important; font-family: var(--font-display) !important; }

hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 1.5rem 0 !important; }

::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--void); }
::-webkit-scrollbar-thumb { background: var(--arcane-dim); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--arcane); }

[data-testid="stExpander"] { background: var(--void-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius) !important; }
[data-testid="stExpander"] summary { color: var(--parchment) !important; font-family: var(--font-display) !important; font-size: 0.85rem !important; letter-spacing: 0.04em !important; }

[data-testid="stProgress"] > div > div { background: var(--void-3) !important; border-radius: 20px !important; }
[data-testid="stProgress"] > div > div > div { background: linear-gradient(90deg, var(--arcane-dim), var(--arcane), var(--arcane-2)) !important; border-radius: 20px !important; box-shadow: 0 0 10px var(--arcane-glow) !important; }

[data-testid="stFileUploader"] { background: var(--void-2) !important; border: 2px dashed var(--border) !important; border-radius: var(--radius-lg) !important; padding: 1.5rem !important; transition: border-color 0.2s !important; }
[data-testid="stFileUploader"]:hover { border-color: var(--arcane) !important; }
[data-testid="stFileUploader"] label { color: var(--parchment-3) !important; font-family: var(--font-display) !important; font-size: 0.82rem !important; letter-spacing: 0.04em !important; }

[data-testid="stChatInput"] textarea { background-color: var(--void-3) !important; border: 1px solid var(--border) !important; color: var(--parchment) !important; border-radius: var(--radius) !important; }
[data-testid="stChatMessage"] { background: var(--void-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-lg) !important; }

[data-testid="stForm"] { background: var(--ghost) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-lg) !important; padding: 1.5rem !important; }

.stAlert { border-radius: var(--radius) !important; }

[data-testid="stMainBlockContainer"] { padding-top: 1rem !important; }
</style>
"""

# ── Master CSS Part 4: Animations ─────────────────────────────────────────────
THEME_CSS_4 = """
<style>
@keyframes arcane-pulse {
    0%, 100% { box-shadow: 0 0 15px rgba(123,47,255,0.3); }
    50%       { box-shadow: 0 0 35px rgba(123,47,255,0.7), 0 0 60px rgba(123,47,255,0.2); }
}
@keyframes gold-shimmer {
    0%, 100% { opacity: 0.7; }
    50%       { opacity: 1; }
}
@keyframes rune-float {
    0%, 100% { transform: translateY(0px); opacity: 0.6; }
    50%       { transform: translateY(-6px); opacity: 1; }
}
@keyframes scan-line {
    0%   { top: 0%; }
    100% { top: 100%; }
}
@keyframes fade-in-up {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes ember-glow {
    0%, 100% { text-shadow: 0 0 8px rgba(201,168,76,0.5); }
    50%       { text-shadow: 0 0 20px rgba(201,168,76,0.9), 0 0 40px rgba(201,168,76,0.3); }
}
@keyframes slide-in-right {
    from { opacity: 0; transform: translateX(20px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes reveal-scroll {
    from { opacity: 0; transform: scaleY(0.85) translateY(-10px); }
    to   { opacity: 1; transform: scaleY(1) translateY(0); }
}
.animate-fade-up  { animation: fade-in-up 0.5s ease forwards; }
.animate-slide-in { animation: slide-in-right 0.4s ease forwards; }
.animate-scroll   { animation: reveal-scroll 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }
</style>
"""


# ── inject_theme ──────────────────────────────────────────────────────────────
def inject_theme():
    """Call once at the top of every page function."""
    st.markdown(FONTS_HTML, unsafe_allow_html=True)
    st.markdown(THEME_CSS_1, unsafe_allow_html=True)
    st.markdown(THEME_CSS_2, unsafe_allow_html=True)
    st.markdown(THEME_CSS_3, unsafe_allow_html=True)
    st.markdown(THEME_CSS_4, unsafe_allow_html=True)


# ── Ambient void background with floating runes ───────────────────────────────
def ambient_bg():
    """Injects a subtle animated starfield + rune particles behind the app."""
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"]::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background:
            radial-gradient(ellipse at 20% 50%, rgba(123,47,255,0.06) 0%, transparent 60%),
            radial-gradient(ellipse at 80% 20%, rgba(201,168,76,0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 60% 80%, rgba(26,188,156,0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    </style>
    """, unsafe_allow_html=True)


# ── Page header ───────────────────────────────────────────────────────────────
def page_header(title: str, subtitle: str = "", icon: str = "📜", animate: bool = True):
    """Dramatic RPG page header with Cinzel, gold divider, and rune ornament."""
    anim = 'animation: fade-in-up 0.6s ease forwards;' if animate else ''
    subtitle_html = (
        f'<p style="color:#8a7050;font-size:0.88rem;margin:0.4rem 0 0;'
        f'letter-spacing:0.06em;font-style:italic;">{subtitle}</p>'
    ) if subtitle else ""
    st.markdown(f"""
    <div style="text-align:center;padding:1.8rem 0 1rem;{anim}">
        <div style="font-size:3rem;margin-bottom:0.5rem;
                    filter:drop-shadow(0 0 12px rgba(201,168,76,0.5));
                    animation:rune-float 3s ease-in-out infinite;">{icon}</div>
        <h1 style="font-family:'Cinzel Decorative',serif;color:#c9a84c;
                   font-size:1.9rem;letter-spacing:0.1em;margin:0;
                   text-shadow:0 0 30px rgba(201,168,76,0.3),0 2px 4px rgba(0,0,0,0.5);">
            {title}
        </h1>
        {subtitle_html}
        <div style="margin:1rem auto 0;width:180px;height:1px;
                    background:linear-gradient(90deg,transparent,#c9a84c88,#c9a84c,#c9a84c88,transparent);">
        </div>
        <div style="margin:0.4rem auto;display:flex;justify-content:center;gap:8px;
                    color:#c9a84c55;font-size:0.7rem;letter-spacing:0.4em;">
            ✦ · · · ✦ · · · ✦
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── RPG Card ──────────────────────────────────────────────────────────────────
def rpg_card(title: str, body: str, accent: str = "arcane", footer: str = "", animate: bool = False):
    colors = {
        "arcane": ("rgba(123,47,255,0.18)", "#7b2fff",  "rgba(123,47,255,0.08)"),
        "gold":   ("rgba(201,168,76,0.18)",  "#c9a84c", "rgba(201,168,76,0.06)"),
        "ember":  ("rgba(192,57,43,0.18)",   "#c0392b", "rgba(192,57,43,0.06)"),
        "teal":   ("rgba(26,188,156,0.18)",  "#1abc9c", "rgba(26,188,156,0.06)"),
    }
    border_color, glow_color, bg_tint = colors.get(accent, colors["arcane"])
    anim = "animation:fade-in-up 0.4s ease forwards;" if animate else ""

    footer_html = ""
    if footer:
        footer_html = (
            f'<div style="margin-top:10px;padding-top:10px;'
            f'border-top:1px solid {border_color};'
            f'color:#8a7050;font-size:0.76rem;">{footer}</div>'
        )

    html = (
        f'<div style="background:linear-gradient(135deg,#0d0a1f,#100d1c);'
        f'border:1px solid {border_color};border-radius:14px;'
        f'padding:1.2rem 1.4rem;margin:0.5rem 0;'
        f'position:relative;overflow:hidden;{anim}'
        f'box-shadow:inset 0 0 40px rgba(0,0,0,0.5),0 4px 20px rgba(0,0,0,0.3);">'
        f'<div style="position:absolute;inset:0;background:{bg_tint};pointer-events:none;"></div>'
        f'<div style="position:absolute;top:0;left:15px;right:15px;height:1px;'
        f'background:linear-gradient(90deg,transparent,{glow_color}88,transparent);"></div>'
        f'<h3 style="font-family:Cinzel,serif;color:#c9a84c;font-size:0.92rem;'
        f'letter-spacing:0.07em;margin:0 0 8px;position:relative;">{title}</h3>'
        f'<div style="color:#e8d5b0;font-size:0.88rem;line-height:1.65;position:relative;">{body}</div>'
        f'{footer_html}'
        f'<div style="position:absolute;bottom:0;left:15px;right:15px;height:1px;'
        f'background:linear-gradient(90deg,transparent,{glow_color}55,transparent);"></div>'
        f'</div>'
    )

    st.markdown(html, unsafe_allow_html=True)
    
# ── Scholar Hero Card ─────────────────────────────────────────────────────────
def scholar_hero_card(scholar: dict, rank_info: dict, next_xp: int):
    """Large hero card shown on the academy dashboard."""
    xp = scholar.get("total_xp", 0)
    pct = min(100, int((xp / max(next_xp, 1)) * 100)) if next_xp else 100
    streak = scholar.get("current_streak", 0)
    rank_num = scholar.get("rank", 1)

    rank_colors = {1:"#8a7050", 2:"#7b2fff", 3:"#1abc9c", 4:"#c9a84c", 5:"#c0392b"}
    glow = rank_colors.get(rank_num, "#7b2fff")

    next_xp_display = f"{next_xp} XP" if next_xp else "MAX"
    remaining = (next_xp - xp) if next_xp else 0
    remaining_text = f"{remaining} XP to rank up" if next_xp else "Chrono-Legend — Peak reached"

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0a0618 0%,#110c24 50%,#0d0a1a 100%);
                border:1px solid {glow}44;border-radius:20px;
                padding:1.8rem 2rem;margin:0.8rem 0;
                box-shadow:0 0 40px {glow}22,inset 0 0 60px rgba(0,0,0,0.6);
                position:relative;overflow:hidden;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;
                    background:linear-gradient(90deg,transparent,{glow}aa,{glow},{glow}aa,transparent);"></div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:1px;
                    background:linear-gradient(90deg,transparent,{glow}44,transparent);"></div>
        <div style="position:absolute;top:-40px;right:-40px;width:150px;height:150px;
                    background:radial-gradient(circle,{glow}18,transparent 70%);
                    pointer-events:none;"></div>
        <div style="display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;">
            <div style="font-size:3.5rem;filter:drop-shadow(0 0 15px {glow}88);
                        animation:rune-float 4s ease-in-out infinite;">
                {rank_info['emoji']}
            </div>
            <div style="flex:1;min-width:180px;">
                <div style="font-family:'Cinzel Decorative',serif;color:#c9a84c;
                            font-size:1.4rem;font-weight:700;
                            text-shadow:0 0 20px rgba(201,168,76,0.4);
                            letter-spacing:0.06em;margin-bottom:2px;">
                    {scholar['name']}
                </div>
                <div style="font-family:'Cinzel',serif;color:{glow};font-size:0.82rem;
                            letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.6rem;">
                    {rank_info['title']}
                </div>
                <div style="display:flex;gap:12px;flex-wrap:wrap;">
                    <span style="background:{glow}22;border:1px solid {glow}44;
                                 color:{glow};border-radius:20px;padding:3px 12px;
                                 font-size:0.72rem;font-family:'JetBrains Mono',monospace;">
                        ⚡ {xp} XP
                    </span>
                    <span style="background:rgba(123,47,255,0.15);border:1px solid rgba(123,47,255,0.3);
                                 color:#9b7fff;border-radius:20px;padding:3px 12px;
                                 font-size:0.72rem;font-family:'JetBrains Mono',monospace;">
                        🔥 {streak}-day streak
                    </span>
                </div>
            </div>
        </div>
        <div style="margin-top:1.2rem;">
            <div style="display:flex;justify-content:space-between;
                        margin-bottom:6px;align-items:center;">
                <span style="font-family:'Cinzel',serif;color:#8a7050;
                             font-size:0.72rem;letter-spacing:0.06em;text-transform:uppercase;">
                    Rank Progress
                </span>
                <span style="font-family:'JetBrains Mono',monospace;color:#5a4830;font-size:0.7rem;">
                    {xp} / {next_xp_display}
                </span>
            </div>
            <div style="background:#0d0a1f;border:1px solid {glow}33;
                        border-radius:20px;height:8px;overflow:hidden;">
                <div style="width:{pct}%;height:100%;
                            background:linear-gradient(90deg,{glow}88,{glow});
                            border-radius:20px;
                            box-shadow:0 0 10px {glow}88;
                            transition:width 1s ease;"></div>
            </div>
            <div style="text-align:right;margin-top:4px;
                        font-size:0.68rem;color:#5a4830;
                        font-family:'JetBrains Mono',monospace;">
                {remaining_text}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── XP Bar (standalone, for backward compat) ─────────────────────────────────
def xp_bar(current_xp: int, next_threshold: int, rank_title: str, rank_num: int):
    """Animated XP progress bar — kept for backward compatibility."""
    pct = min(100, int((current_xp / max(next_threshold, 1)) * 100))
    remaining = next_threshold - current_xp
    st.markdown(f"""
    <div style="margin:0.8rem 0;">
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;">
            <span style="font-family:'Cinzel',serif;color:#c9a84c;font-size:0.8rem;letter-spacing:0.05em;">
                ✦ {rank_title}
            </span>
            <span style="font-family:'JetBrains Mono',monospace;color:#8a7050;font-size:0.75rem;">
                {current_xp} / {next_threshold} XP
            </span>
        </div>
        <div style="background:#1a1530;border:1px solid rgba(123,47,255,0.35);
                    border-radius:20px;height:10px;overflow:hidden;">
            <div style="width:{pct}%;height:100%;
                        background:linear-gradient(90deg,#3d1880,#7b2fff,#9b5fff);
                        border-radius:20px;box-shadow:0 0 10px rgba(123,47,255,0.6);"></div>
        </div>
        <div style="text-align:right;margin-top:4px;font-size:0.72rem;color:#8a7050;
                    font-family:'JetBrains Mono',monospace;">
            {remaining} XP to next rank
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Stat Pill ─────────────────────────────────────────────────────────────────
def stat_pill(label: str, value: str, color: str = "arcane"):
    """Inline stat pill — use in a st.columns layout."""
    colors = {
        "arcane": ("#0f0620", "#7b2fff", "#c8a8ff"),
        "gold":   ("#110d00", "#c9a84c", "#f5e199"),
        "ember":  ("#160300", "#c0392b", "#ffb0a8"),
        "teal":   ("#001512", "#1abc9c", "#a0ffe8"),
    }
    bg, border, text = colors.get(color, colors["arcane"])
    st.markdown(f"""
    <div style="background:{bg};border:1px solid {border}55;
                border-radius:12px;padding:10px 14px;
                text-align:center;margin:4px 0;
                box-shadow:inset 0 0 20px rgba(0,0,0,0.4);">
        <div style="color:{border};font-size:0.62rem;font-family:'Cinzel',serif;
                    letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;">
            {label}
        </div>
        <div style="color:{text};font-family:'JetBrains Mono',monospace;
                    font-size:1.3rem;font-weight:500;">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Quest Scroll ──────────────────────────────────────────────────────────────
def quest_scroll(title: str, topic: str, difficulty: str, num_questions: int):
    """A sealed scroll card for the quest intro page."""
    diff_config = {
        "easy":      ("⚗️", "#1abc9c", "Apprentice Trial"),
        "medium":    ("🔮", "#7b2fff", "Seeker's Path"),
        "hard":      ("⚔️", "#c9a84c", "Master's Ordeal"),
        "legendary": ("💀", "#c0392b", "Chrono-Legend"),
    }
    icon, color, label = diff_config.get(difficulty, diff_config["medium"])
    st.markdown(f"""
    <div style="background:linear-gradient(160deg,#05030f 0%,#0d0a1f 50%,#08051a 100%);
                border:1px solid {color}44;border-radius:18px;
                padding:2.2rem 2rem;text-align:center;
                margin:1rem 0;position:relative;overflow:hidden;
                animation:reveal-scroll 0.6s cubic-bezier(0.34,1.56,0.64,1) forwards;
                box-shadow:0 0 60px {color}15,inset 0 0 80px rgba(0,0,0,0.6);">
        <div style="position:absolute;top:0;left:0;right:0;height:3px;
                    background:linear-gradient(90deg,transparent,{color},{color}cc,{color},transparent);
                    box-shadow:0 0 15px {color};">
        </div>
        <div style="font-size:3rem;margin-bottom:0.8rem;
                    filter:drop-shadow(0 0 20px {color}88);
                    animation:rune-float 3s ease-in-out infinite;">{icon}</div>
        <div style="font-family:'Cinzel Decorative',serif;color:#c9a84c;
                    font-size:1.35rem;font-weight:700;letter-spacing:0.08em;
                    margin-bottom:0.4rem;
                    text-shadow:0 0 25px rgba(201,168,76,0.5);">
            {title}
        </div>
        <div style="color:#8a7050;font-size:0.85rem;margin-bottom:1.5rem;
                    font-style:italic;letter-spacing:0.03em;">{topic}</div>
        <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
            <span style="background:{color}18;border:1px solid {color}44;
                         color:{color};border-radius:20px;padding:5px 18px;
                         font-size:0.76rem;font-family:'Cinzel',serif;letter-spacing:0.07em;">
                {label}
            </span>
            <span style="background:rgba(201,168,76,0.1);border:1px solid rgba(201,168,76,0.3);
                         color:#c9a84c;border-radius:20px;padding:5px 18px;
                         font-size:0.76rem;font-family:'JetBrains Mono',monospace;">
                {num_questions} Trials
            </span>
        </div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:2px;
                    background:linear-gradient(90deg,transparent,{color}44,transparent);"></div>
    </div>
    """, unsafe_allow_html=True)


# ── Notification Toast ────────────────────────────────────────────────────────
def notification_toast(message: str, kind: str = "info"):
    """Floating notification banner."""
    config = {
        "info":    ("#0d0a1f", "#7b2fff", "📜"),
        "success": ("#031208", "#1abc9c", "✦"),
        "warning": ("#120e00", "#c9a84c", "⚠"),
        "danger":  ("#120200", "#c0392b", "✕"),
    }
    bg, border, icon = config.get(kind, config["info"])
    st.markdown(f"""
    <div style="background:{bg};border:1px solid {border}44;
                border-left:3px solid {border};
                border-radius:10px;padding:12px 16px;
                display:flex;align-items:flex-start;gap:10px;
                margin:6px 0;color:#e8d5b0;font-size:0.87rem;
                line-height:1.5;
                box-shadow:0 4px 20px rgba(0,0,0,0.4);">
        <span style="color:{border};font-size:1rem;flex-shrink:0;margin-top:1px;">{icon}</span>
        <span>{message}</span>
    </div>
    """, unsafe_allow_html=True)


# ── Challenge Arena Card ──────────────────────────────────────────────────────
def challenge_arena(question: str, trial_num: int, total: int):
    """Dramatic challenge header for the quiz page."""
    from backend.translations import t

    trial_label = t("trial_of", current=trial_num, total=total)

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#08051a,#110c24,#08051a);
                border:1px solid rgba(123,47,255,0.35);border-radius:16px;
                padding:1.8rem 1.6rem;margin:0.5rem 0 1rem;
                position:relative;overflow:hidden;
                box-shadow:0 0 40px rgba(123,47,255,0.15),inset 0 0 60px rgba(0,0,0,0.5);
                animation:arcane-pulse 3s ease-in-out infinite;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;
                    background:linear-gradient(90deg,transparent,#7b2fff,#9b4fff,#7b2fff,transparent);"></div>
        <div style="display:flex;justify-content:space-between;align-items:center;
                    margin-bottom:1rem;">
            <div style="font-family:'Cinzel',serif;color:#7b2fff;font-size:0.72rem;
                        letter-spacing:0.15em;text-transform:uppercase;">
                {trial_label}
            </div>
            <div style="display:flex;gap:6px;">
                {"".join(f'<div style="width:22px;height:4px;border-radius:2px;background:{"#7b2fff" if i < trial_num else "#1e1640"};box-shadow:{"0 0 8px #7b2fff88" if i < trial_num else "none"};"></div>' for i in range(total))}
            </div>
        </div>
        <div style="font-family:'Cinzel',serif;color:#e8d5b0;font-size:1.05rem;
                    line-height:1.6;letter-spacing:0.03em;">
            {question}
        </div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:1px;
                    background:linear-gradient(90deg,transparent,rgba(123,47,255,0.3),transparent);"></div>
    </div>
    """, unsafe_allow_html=True)

# ── Sidebar Scholar Panel ─────────────────────────────────────────────────────
def sidebar_scholar_panel(scholar: dict, rank_info: dict):
    """Compact scholar info for the sidebar."""
    streak = scholar.get("current_streak", 0)
    xp = scholar.get("total_xp", 0)
    rank_num = scholar.get("rank", 1)
    rank_colors = {1:"#8a7050", 2:"#7b2fff", 3:"#1abc9c", 4:"#c9a84c", 5:"#c0392b"}
    glow = rank_colors.get(rank_num, "#7b2fff")

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0a0618,#0d0a1f);
                border:1px solid {glow}33;border-radius:14px;
                padding:1rem 1.1rem;margin-bottom:0.8rem;
                box-shadow:0 0 20px {glow}11;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.7rem;">
            <span style="font-size:1.8rem;filter:drop-shadow(0 0 8px {glow}88);">
                {rank_info['emoji']}
            </span>
            <div>
                <div style="font-family:'Cinzel',serif;color:#c9a84c;
                            font-size:0.85rem;font-weight:600;">
                    {scholar['name']}
                </div>
                <div style="font-family:'Cinzel',serif;color:{glow};
                            font-size:0.65rem;letter-spacing:0.08em;text-transform:uppercase;">
                    {rank_info['title']}
                </div>
            </div>
        </div>
        <div style="display:flex;justify-content:space-between;">
            <div style="text-align:center;">
                <div style="font-family:'JetBrains Mono',monospace;color:#c9a84c;font-size:0.9rem;">
                    {xp}
                </div>
                <div style="font-size:0.6rem;color:#5a4830;letter-spacing:0.06em;text-transform:uppercase;">
                    XP
                </div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'JetBrains Mono',monospace;color:#9b7fff;font-size:0.9rem;">
                    🔥 {streak}
                </div>
                <div style="font-size:0.6rem;color:#5a4830;letter-spacing:0.06em;text-transform:uppercase;">
                    Streak
                </div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'JetBrains Mono',monospace;color:{glow};font-size:0.9rem;">
                    {rank_num}/5
                </div>
                <div style="font-size:0.6rem;color:#5a4830;letter-spacing:0.06em;text-transform:uppercase;">
                    Rank
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Results Trophy Card ───────────────────────────────────────────────────────
def results_trophy(score: int, total: int, xp: int, badge: str, perfect: bool = False):
    """Grand results card shown on the quest completion screen."""
    pct = int((score / max(total, 1)) * 100)
    if perfect:
        glow_color = "#c9a84c"
        title_text = "FLAWLESS VICTORY"
        stars = "★ ★ ★"
    elif pct >= 60:
        glow_color = "#7b2fff"
        title_text = "DIMENSION CONQUERED"
        stars = "★ ★ ☆"
    else:
        glow_color = "#1abc9c"
        title_text = "TRIAL COMPLETE"
        stars = "★ ☆ ☆"

    st.markdown(f"""
    <div style="background:linear-gradient(160deg,#05030f,#0f0a20,#05030f);
                border:2px solid {glow_color}55;border-radius:20px;
                padding:2.5rem 2rem;text-align:center;
                margin:1rem 0;position:relative;overflow:hidden;
                animation:fade-in-up 0.6s ease forwards;
                box-shadow:0 0 60px {glow_color}22,inset 0 0 80px rgba(0,0,0,0.6);">
        <div style="position:absolute;top:0;left:0;right:0;height:3px;
                    background:linear-gradient(90deg,transparent,{glow_color},{glow_color}cc,transparent);
                    box-shadow:0 0 20px {glow_color};"></div>
        <div style="font-size:3.5rem;margin-bottom:0.5rem;
                    filter:drop-shadow(0 0 20px {glow_color}aa);
                    animation:rune-float 3s ease-in-out infinite;">🏆</div>
        <div style="font-family:'Cinzel Decorative',serif;color:{glow_color};
                    font-size:1.3rem;font-weight:700;letter-spacing:0.12em;
                    margin-bottom:0.3rem;
                    text-shadow:0 0 30px {glow_color}88;">
            {title_text}
        </div>
        <div style="color:{glow_color}88;font-size:1.1rem;margin-bottom:1.2rem;
                    letter-spacing:0.3em;">{stars}</div>
        <div style="display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;margin:1rem 0;">
            <div>
                <div style="font-family:'JetBrains Mono',monospace;color:#c9a84c;font-size:2rem;font-weight:500;">
                    {score}/{total}
                </div>
                <div style="font-size:0.68rem;color:#8a7050;letter-spacing:0.1em;text-transform:uppercase;">
                    Correct
                </div>
            </div>
            <div>
                <div style="font-family:'JetBrains Mono',monospace;color:#7b2fff;font-size:2rem;font-weight:500;">
                    +{xp}
                </div>
                <div style="font-size:0.68rem;color:#8a7050;letter-spacing:0.1em;text-transform:uppercase;">
                    XP Earned
                </div>
            </div>
        </div>
        <div style="background:{glow_color}15;border:1px solid {glow_color}33;
                    border-radius:10px;padding:10px 16px;margin-top:0.8rem;
                    font-family:'Cinzel',serif;color:{glow_color};
                    font-size:0.78rem;letter-spacing:0.06em;">
            🎖️ {badge}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Login Atmosphere ──────────────────────────────────────────────────────────
def login_atmosphere():
    """Decorative header for the login/register page."""
    from backend.translations import t
    st.markdown(f"""
    <div style="text-align:center;padding:2rem 0 0.5rem;position:relative;">
        <div style="position:relative;display:inline-block;">
            <div style="font-family:'Cinzel Decorative',serif;color:#c9a84c;
                        font-size:2.4rem;font-weight:700;
                        text-shadow:0 0 40px rgba(201,168,76,0.5),0 0 80px rgba(201,168,76,0.2);
                        letter-spacing:0.1em;
                        animation:ember-glow 3s ease-in-out infinite;">
                {t("academy_name_line1")}
            </div>
            <div style="font-family:'Cinzel Decorative',serif;color:#9b4fff;
                        font-size:2.8rem;font-weight:700;
                        text-shadow:0 0 40px rgba(123,47,255,0.6),0 0 80px rgba(123,47,255,0.2);
                        letter-spacing:0.15em;margin-top:-0.2rem;
                        animation:arcane-pulse 4s ease-in-out infinite;">
                {t("academy_name_line2")}
            </div>
        </div>
        <div style="margin:0.8rem auto;width:280px;height:1px;
                    background:linear-gradient(90deg,transparent,#7b2fff,#c9a84c,#7b2fff,transparent);">
        </div>
        <div style="color:#5a4830;font-size:0.78rem;letter-spacing:0.2em;font-family:'Cinzel',serif;
                    text-transform:uppercase;margin-bottom:0.5rem;">
            ✦ {t("academy_subtitle")} ✦
        </div>
        <div style="display:flex;justify-content:center;gap:24px;margin-top:0.8rem;
                    font-size:1.5rem;opacity:0.5;">
            <span style="animation:rune-float 3s ease-in-out infinite;">🔮</span>
            <span style="animation:rune-float 3.5s ease-in-out 0.5s infinite;">📜</span>
            <span style="animation:rune-float 4s ease-in-out 1s infinite;">⚔️</span>
            <span style="animation:rune-float 3.2s ease-in-out 1.5s infinite;">🌀</span>
            <span style="animation:rune-float 3.8s ease-in-out 0.8s infinite;">✨</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
# ── NPC Dialogue Box ──────────────────────────────────────────────────────────
def npc_dialogue(npc_name: str, text: str, icon: str = "🧙"):
    """Textbox-style NPC dialogue for quest intros and hints."""
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#080514,#0f0c22);
                border:1px solid rgba(123,47,255,0.35);border-radius:14px;
                padding:1.2rem 1.4rem;margin:0.8rem 0;
                position:relative;
                box-shadow:inset 0 0 30px rgba(0,0,0,0.5),0 4px 20px rgba(0,0,0,0.3);
                animation:fade-in-up 0.4s ease forwards;">
        <div style="position:absolute;top:-1px;left:20px;right:20px;height:1px;
                    background:linear-gradient(90deg,transparent,rgba(123,47,255,0.5),transparent);"></div>
        <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="font-size:2rem;flex-shrink:0;
                        filter:drop-shadow(0 0 10px rgba(123,47,255,0.6));">{icon}</div>
            <div style="flex:1;">
                <div style="font-family:'Cinzel',serif;color:#7b2fff;font-size:0.72rem;
                            letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;">
                    {npc_name}
                </div>
                <div style="color:#c4aa7a;font-size:0.9rem;line-height:1.65;font-style:italic;">
                    "{text}"
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Section divider with rune ─────────────────────────────────────────────────
def rune_divider(label: str = ""):
    """Decorative divider with optional label."""
    if label:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:12px;margin:1.2rem 0;">
            <div style="flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(123,47,255,0.3));"></div>
            <div style="font-family:'Cinzel',serif;color:#5a4830;font-size:0.7rem;
                        letter-spacing:0.12em;text-transform:uppercase;white-space:nowrap;">
                {label}
            </div>
            <div style="flex:1;height:1px;background:linear-gradient(90deg,rgba(123,47,255,0.3),transparent);"></div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:8px;margin:1rem 0;">
            <div style="flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(123,47,255,0.25));"></div>
            <div style="color:rgba(123,47,255,0.4);font-size:0.7rem;">✦</div>
            <div style="flex:1;height:1px;background:linear-gradient(90deg,rgba(123,47,255,0.25),transparent);"></div>
        </div>
        """, unsafe_allow_html=True)