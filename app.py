import streamlit as st
import json
import time
from groq import Groq
import os
from dotenv import load_dotenv
from backend.database import (
    init_db, create_scholar, get_scholar, name_exists,
    add_xp, get_rank_info, get_xp_for_next_rank,
    create_dimension, complete_dimension, get_scholar_dimensions,
    save_message, get_chat_history
)
from backend.streak_migration import apply_streak_migration
from backend.quest_generator import generate_quest, validate_quest
from ui.streak_ui import handle_login_streak, render_streak_panel, render_streak_badge
from backend.chronicler_prompts import build_chat_messages
from ui.theme import (
    inject_theme, page_header, rpg_card, notification_toast,
    xp_bar, stat_pill, quest_scroll, scholar_hero_card,
    challenge_arena, sidebar_scholar_panel, results_trophy,
    login_atmosphere, npc_dialogue, rune_divider, ambient_bg
)
from ui.language_selector import render_language_selector
from backend.translations import (
    t, translated_theme_options, translated_difficulty_options,
    theme_display_to_english, difficulty_display_to_english,
)
from ui.difficulty_toggle import render_difficulty_toggle 

load_dotenv()

# ── Init ──────────────────────────────────────────────────────
init_db()

apply_streak_migration()

# ── App config ────────────────────────────────────────────────
st.set_page_config(
    page_title="The Chronicler's Academy",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_theme()
ambient_bg()

# ── Session state ─────────────────────────────────────────────
defaults = {
    "page": "login",
    "scholar": None,
    "lesson_text": "",
    "pdf_name": "",
    "quest": None,
    "dimension_id": None,
    "current_challenge": 0,
    "score": 0,
    "hints_used": 0,
    "show_hint": False,
    "answer_submitted": False,
    "last_answer_correct": None,
    "chat_messages": [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Helpers ───────────────────────────────────────────────────
def go_to(page):
    st.session_state.page = page
    st.rerun()

def calculate_xp(score, total, hints_used):
    xp = 50
    xp += score * 30
    if hints_used == 0:
        xp += 20
    if score == total:
        xp += 50
    return xp

def _build_sidebar(scholar):
    """Render persistent sidebar for logged-in scholars."""
    from backend.translations import t

    rank_info = get_rank_info(scholar["rank"])
    with st.sidebar:
        sidebar_scholar_panel(scholar, rank_info)
        rune_divider()
        st.markdown(
            f'<div style="font-family:\'Cinzel\',serif;color:#5a4830;font-size:0.65rem;'
            f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.5rem;">{t("sidebar_navigation")}</div>',
            unsafe_allow_html=True
        )
        if st.button(t("nav_academy"), use_container_width=True, key="nav_academy"):
            go_to("academy")
        if st.button(t("nav_new_dimension"), use_container_width=True, key="nav_upload"):
            st.session_state.lesson_text = ""
            st.session_state.pdf_name = ""
            st.session_state.quest = None
            st.session_state.chat_messages = []
            go_to("upload")
        if st.button(t("nav_archive"), use_container_width=True, key="nav_archive"):
            go_to("archive")
        rune_divider()
        if st.button(t("nav_logout"), use_container_width=True,
                     type="secondary", key="nav_logout"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
# ── Pages ─────────────────────────────────────────────────────

def page_login():
    render_language_selector()
    login_atmosphere()
 
    tab1, tab2 = st.tabs([t("tab_returning"), t("tab_new")])
 
    with tab1:
        st.markdown(
            f'<p style="color:#8a7050;font-size:0.82rem;letter-spacing:0.04em;'
            f'font-family:\'Cinzel\',serif;margin-bottom:1rem;">{t("welcome_back")}</p>',
            unsafe_allow_html=True
        )
        with st.form("login_form"):
            name = st.text_input(t("label_scholar_name"), placeholder="...")
            pin  = st.text_input(t("label_pin"), type="password", max_chars=4,
                                 placeholder="••••")
            submitted = st.form_submit_button(t("btn_enter_academy"),
                                              use_container_width=True)
            if submitted:
                if not name or not pin:
                    notification_toast(t("error_name_pin_required"), kind="warning")
                else:
                    scholar = get_scholar(name, pin)
                    if scholar:
                        st.session_state.scholar = scholar
                        handle_login_streak(scholar)
                        go_to("academy")
                    else:
                        notification_toast(t("error_scholar_not_found"), kind="danger")
 
    with tab2:
        st.markdown(
            f'<p style="color:#8a7050;font-size:0.82rem;letter-spacing:0.04em;'
            f'font-family:\'Cinzel\',serif;margin-bottom:1rem;">{t("begin_journey")}</p>',
            unsafe_allow_html=True
        )
        with st.form("register_form"):
            name       = st.text_input(t("label_choose_name"), placeholder="...")
            pin        = st.text_input(t("label_choose_pin"), type="password", max_chars=4)
            pin2       = st.text_input(t("label_confirm_pin"), type="password", max_chars=4)
            theme_display = st.selectbox(t("label_theme"), translated_theme_options())
            difficulty_display = st.select_slider(t("label_difficulty"), options=translated_difficulty_options())
            interests  = st.text_input(t("label_interests"),
                                       placeholder=t("placeholder_interests"))
            want_quiz  = st.checkbox(t("label_want_quiz"))
            submitted  = st.form_submit_button(t("btn_create_scholar"), use_container_width=True)
            if submitted:
                theme = theme_display_to_english(theme_display)
                difficulty = difficulty_display_to_english(difficulty_display)
                if not name:
                    notification_toast(t("error_choose_name"), kind="warning")
                elif not pin or len(pin) != 4 or not pin.isdigit():
                    notification_toast(t("error_pin_length"), kind="warning")
                elif pin != pin2:
                    notification_toast(t("error_pin_mismatch"), kind="danger")
                elif name_exists(name):
                    notification_toast(t("error_name_taken"), kind="danger")
                else:
                    st.session_state._new_scholar_data = {
                        "name": name, "pin": pin,
                        "theme": theme, "difficulty": difficulty,
                        "interests": interests or theme,
                        "want_quiz": want_quiz
                    }
                    if want_quiz:
                        go_to("quiz")
                    else:
                        data = st.session_state._new_scholar_data
                        create_scholar(
                            data["name"], data["pin"],
                            data["theme"], data["difficulty"],
                            data["interests"]
                        )
                        scholar = get_scholar(data["name"], data["pin"])
                        st.session_state.scholar = scholar
                        go_to("academy")

def page_quiz():
    from backend.translations import t, translated_quiz_options, quiz_display_to_english

    page_header(t("quiz_title"), subtitle=t("quiz_subtitle"), icon="🎯")

    rune_divider(t("quiz_divider"))

    with st.form("quiz_form"):
        q1 = st.radio(t("quiz_q1"), translated_quiz_options("q1"))
        q2 = st.radio(t("quiz_q2"), translated_quiz_options("q2"))
        q3 = st.radio(t("quiz_q3"), translated_quiz_options("q3"))
        q4 = st.radio(t("quiz_q4"), translated_quiz_options("q4"))
        submitted = st.form_submit_button(t("btn_seal_path"), use_container_width=True)
        if submitted:
            # Convert displayed (translated) answers back to English for storage
            q1_en = quiz_display_to_english("q1", q1)
            q2_en = quiz_display_to_english("q2", q2)
            q3_en = quiz_display_to_english("q3", q3)
            q4_en = quiz_display_to_english("q4", q4)

            data = st.session_state._new_scholar_data
            interests_enriched = (
                f"{data['interests']}, play style: {q1_en}, "
                f"hero type: {q4_en}, quest style: {q3_en}"
            )
            create_scholar(
                data["name"], data["pin"],
                data["theme"], data["difficulty"],
                interests_enriched,
                play_style=q1_en, hero_type=q4_en,
                quest_style=q3_en, reward_preference=q2_en
            )
            scholar = get_scholar(data["name"], data["pin"])
            st.session_state.scholar = scholar
            go_to("academy")

def page_academy():
    from backend.translations import t

    scholar     = st.session_state.scholar
    rank_info   = get_rank_info(scholar["rank"])
    next_xp     = get_xp_for_next_rank(scholar["rank"])
    dimensions  = get_scholar_dimensions(scholar["id"])

    _build_sidebar(scholar)

    page_header(t("academy_page_title_text"),
                subtitle=t("welcome_back_name", name=scholar['name']),
                icon=rank_info["emoji"])

    # Streak panel
    render_streak_panel(scholar)

    # Hero card
    scholar_hero_card(scholar, rank_info, next_xp or scholar["total_xp"] + 1)

    rune_divider(t("rune_divider_begin_journey"))

    # Primary action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌀 " + t("btn_new_dimension_text"),
                     use_container_width=True, type="primary", key="btn_new_dim"):
            st.session_state.lesson_text = ""
            st.session_state.pdf_name = ""
            st.session_state.quest = None
            st.session_state.chat_messages = []
            go_to("upload")
    with col2:
        if st.button(t("btn_archive"),
                     use_container_width=True, key="btn_archive"):
            go_to("archive")

    # Recent dimensions
    if dimensions:
        rune_divider(t("rune_divider_recent_dimensions"))
        for dim in dimensions[:3]:
            score_pct = int((dim["score"] / max(dim["total_questions"], 1)) * 100)
            accent = "gold" if score_pct == 100 else "arcane"
            rpg_card(
                title=dim["quest_title"],
                body=(
                    f'<span style="color:#5a4830;">📄</span> {dim["pdf_name"]}&nbsp;&nbsp;'
                    f'<span style="color:#5a4830;">·</span>&nbsp;&nbsp;'
                    f'<span style="color:#7b2fff;">⚡</span> +{dim["xp_earned"]} XP&nbsp;&nbsp;'
                    f'<span style="color:#5a4830;">·</span>&nbsp;&nbsp;'
                    f'<span style="color:#c9a84c;">✅</span> {dim["score"]}/{dim["total_questions"]}'
                ),
                accent=accent,
            )
    else:
        rune_divider()
        notification_toast(t("no_dimensions_long"), kind="info")
        
def page_upload():
    from backend.translations import t

    scholar = st.session_state.scholar
    _build_sidebar(scholar)

    page_header(t("upload_title_text"),
                subtitle=t("upload_subtitle_alt"),
                icon="📜")

    tab1, tab2 = st.tabs([t("tab_upload_pdf"), t("tab_inscribe_text")])

    with tab1:
        uploaded = st.file_uploader(t("label_drop_tome"), type="pdf",
                                    label_visibility="hidden")
        if uploaded:
            import fitz
            pdf  = fitz.open(stream=uploaded.read(), filetype="pdf")
            text = "".join(page.get_text() for page in pdf)
            st.session_state.lesson_text = text
            st.session_state.pdf_name = uploaded.name
            notification_toast(
                t("tome_received_html", filename=uploaded.name, chars=f"{len(text):,}"),
                kind="success"
            )
            with st.expander(t("preview_tome")):
                st.markdown(
                    f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;'
                    f'color:#8a7050;line-height:1.6;">{text[:500]}…</div>',
                    unsafe_allow_html=True
                )

    with tab2:
        pasted = st.text_area(
            t("label_inscribe_lesson"),
            height=260,
            placeholder=t("placeholder_inscribe"),
            label_visibility="collapsed"
        )
        if pasted:
            st.session_state.lesson_text = pasted
            st.session_state.pdf_name = t("manual_inscription")

    rune_divider()
    
    if st.session_state.lesson_text:
        render_difficulty_toggle(scholar)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(t("btn_consult_chronicler_alt"),
                         use_container_width=True, key="btn_chat"):
                go_to("chronicler")
        with col2:
            if st.button(t("btn_generate_quest"),
                         use_container_width=True, type="primary", key="btn_quest"):
                go_to("generating")
    else:
        notification_toast(t("upload_or_inscribe_prompt"), kind="info")

    if st.button(t("btn_back_academy"), use_container_width=True,
                 type="secondary", key="btn_back"):
        go_to("academy")
        
def page_chronicler():
    from backend.translations import t

    scholar   = st.session_state.scholar
    rank_info = get_rank_info(scholar["rank"])
    _build_sidebar(scholar)

    page_header(t("chronicler_title_text"),
                subtitle=t("chronicler_subtitle_alt"),
                icon="🧙")

    # Chat history
    for msg in st.session_state.chat_messages:
        role   = msg["role"]
        avatar = "🧙" if role == "assistant" else "🎓"
        with st.chat_message(role, avatar=avatar):
            st.write(msg["content"])

    user_input = st.chat_input(t("chat_placeholder"))

    if user_input:
        st.session_state.chat_messages.append({"role": "user", "content": user_input})

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        current_language = st.session_state.get("language", "es")

        system_prompt, chat_msgs = build_chat_messages(
            scholar=scholar,
            history=st.session_state.chat_messages,
            new_message=user_input,
            rank_title=rank_info["title"],
            lesson_text=st.session_state.lesson_text,
            language=current_language,
        )
        messages = [{"role": "system", "content": system_prompt}] + chat_msgs
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.85,
            max_tokens=600,
        )
        reply = response.choices[0].message.content
        st.session_state.chat_messages.append({"role": "assistant", "content": reply})
        st.rerun()

    rune_divider()
    render_difficulty_toggle(scholar)
    col1, col2 = st.columns(2)
    with col1:
        if st.button(t("btn_generate_quest_alt"),
                     use_container_width=True, type="primary", key="btn_gen"):
            go_to("generating")
    with col2:
        if st.button(t("btn_back_upload_alt"),
                     use_container_width=True, type="secondary", key="btn_back_upload"):
            go_to("upload")

def page_generating():
    from backend.translations import t

    page_header(t("generating_title_text"),
                subtitle=t("generating_subtitle_alt"),
                icon="🌀")

    st.markdown(f"""
    <div style="text-align:center;padding:1rem 0;
                color:#5a4830;font-family:'Cinzel',serif;
                font-size:0.8rem;letter-spacing:0.1em;animation:gold-shimmer 2s infinite;">
        ✦ &nbsp; {t("consulting_records")} &nbsp; ✦
    </div>
    """, unsafe_allow_html=True)

    with st.spinner(t("spinner_crafting")):
        try:
            scholar = st.session_state.scholar
            profile = {
                "name":       scholar["name"],
                "theme":      scholar["theme"],
                "difficulty": st.session_state.get("selected_difficulty", scholar["difficulty"]),
                "interests":  scholar["interests"],
            }
            quest = generate_quest(profile, st.session_state.lesson_text)

            if validate_quest(quest):
                st.session_state.quest             = quest
                st.session_state.current_challenge = 0
                st.session_state.score             = 0
                st.session_state.hints_used        = 0
                st.session_state.answer_submitted  = False

                dim_id = create_dimension(
                    scholar_id=scholar["id"],
                    pdf_name=st.session_state.pdf_name,
                    subject=quest.get("theme", "Unknown"),
                    quest_title=quest["quest_title"],
                    quest_json=quest
                )
                st.session_state.dimension_id = dim_id
                go_to("quest_intro")
            else:
                notification_toast(t("error_quest_validation"), kind="danger")
                time.sleep(2)
                go_to("upload")
        except Exception as e:
            notification_toast(t("error_generic", error=e), kind="danger")
            if st.button(t("btn_try_again_alt")):
                go_to("upload")

def page_quest_intro():
    from backend.translations import t

    quest   = st.session_state.quest
    scholar = st.session_state.scholar
    _build_sidebar(scholar)

    quest_scroll(
        title=quest["quest_title"],
        topic=quest["theme"],
        difficulty=scholar.get("difficulty", "medium").lower(),
        num_questions=len(quest["challenges"]),
    )

    notification_toast(quest["story_intro"], kind="info")

    rune_divider(t("mission_briefing"))

    rpg_card(
        title=t("learning_objective_title"),
        body=quest["learning_objective"],
        accent="gold"
    )

    npc_dialogue(
        npc_name=quest["npc_name"],
        text=quest["npc_dialogue"]
    )

    rune_divider(t("quest_objectives_text"))

    for step in quest["quest_steps"]:
        st.markdown(
            f'<div style="display:flex;gap:12px;align-items:flex-start;'
            f'padding:8px 0;border-bottom:1px solid rgba(123,47,255,0.1);">'
            f'<span style="font-family:\'JetBrains Mono\',monospace;color:#3d1880;'
            f'font-size:0.75rem;padding-top:2px;min-width:20px;">{step["step_number"]}.</span>'
            f'<div>'
            f'<div style="font-family:\'Cinzel\',serif;color:#c9a84c;font-size:0.82rem;'
            f'letter-spacing:0.04em;">{step["title"]}</div>'
            f'<div style="color:#8a7050;font-size:0.84rem;margin-top:2px;">{step["description"]}</div>'
            f'</div></div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(t("btn_begin_trials_alt"), use_container_width=True, type="primary"):
        st.session_state.current_challenge = 1
        go_to("challenge")

def page_challenge():
    from backend.translations import t

    quest   = st.session_state.quest
    scholar = st.session_state.scholar
    total   = len(quest["challenges"])
    current = st.session_state.current_challenge

    if current > total:
        go_to("results")
        return

    _build_sidebar(scholar)
    challenge = quest["challenges"][current - 1]

    # Arena header
    challenge_arena(challenge["question"], current, total)

    # Answer options
    answer = st.radio(
        t("choose_answer"),
        challenge["options"],
        key=f"challenge_{current}",
        disabled=st.session_state.answer_submitted,
        label_visibility="collapsed",
    )

    # Hint display (persistent if shown)
    if st.session_state.get("show_hint"):
        npc_dialogue(
            npc_name=t("chroniclers_hint"),
            text=challenge["hint"],
            icon="💡"
        )

    if not st.session_state.answer_submitted:
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button(t("btn_submit_answer"), use_container_width=True,
                         type="primary", key="btn_submit"):
                correct = answer == challenge["correct_answer"]
                st.session_state.last_answer_correct = correct
                st.session_state.answer_submitted    = True
                st.session_state.show_hint           = False
                if correct:
                    st.session_state.score += 1
                st.rerun()
        with col2:
            if st.button(t("btn_hint"), use_container_width=True, key="btn_hint"):
                if not st.session_state.get("show_hint"):
                    st.session_state.hints_used += 1
                st.session_state.show_hint = True
                st.rerun()
    else:
        if st.session_state.last_answer_correct:
            notification_toast(
                f'<strong>{t("feedback_correct_prefix")}</strong> {challenge["feedback_correct"]}',
                kind="success"
            )
        else:
            notification_toast(
                f'<strong>{t("feedback_incorrect_prefix")}</strong> {challenge["feedback_incorrect"]}',
                kind="danger"
            )
            notification_toast(
                t("feedback_correct_answer_html", answer=challenge["correct_answer"]),
                kind="info"
            )

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(t("btn_next_trial"), use_container_width=True, type="primary"):
            st.session_state.current_challenge  += 1
            st.session_state.answer_submitted    = False
            st.session_state.last_answer_correct = None
            st.session_state.show_hint           = False
            if st.session_state.current_challenge > total:
                go_to("results")
            else:
                st.rerun()

def page_results():
    from backend.translations import t

    quest    = st.session_state.quest
    scholar  = st.session_state.scholar
    score    = st.session_state.score
    total    = len(quest["challenges"])
    hints    = st.session_state.hints_used
    xp_earned = calculate_xp(score, total, hints)
    perfect   = (score == total)

    _build_sidebar(scholar)

    # Save to DB (guard against double-save on rerun)
    if not st.session_state.get("results_saved"):
        complete_dimension(
            st.session_state.dimension_id,
            score, total, xp_earned, hints
        )
        new_total_xp, new_rank = add_xp(scholar["id"], xp_earned)
        st.session_state.scholar["total_xp"] = new_total_xp
        st.session_state.scholar["rank"]     = new_rank
        st.session_state._old_rank           = scholar["rank"]
        st.session_state._new_rank           = new_rank
        st.session_state._new_total_xp       = new_total_xp
        st.session_state.results_saved       = True
    else:
        new_rank     = st.session_state._new_rank
        new_total_xp = st.session_state._new_total_xp

    rank_info = get_rank_info(new_rank)
    reward    = quest["reward"]

    if perfect:
        st.balloons()

    # Trophy card
    results_trophy(
        score=score, total=total, xp=xp_earned,
        badge=reward["badge_name"], perfect=perfect
    )

    # Stats row
    col1, col2, col3 = st.columns(3)
    with col1:
        stat_pill(t("metric_score"), f"{score}/{total}", "gold")
    with col2:
        stat_pill(t("metric_xp_earned"), f"+{xp_earned}", "arcane")
    with col3:
        stat_pill(t("metric_hints"), str(hints), "teal")

    rune_divider()

    # Rank-up check
    old_rank = st.session_state.get("_old_rank", scholar["rank"])
    if new_rank > old_rank:
        rpg_card(
            title=t("rank_up_title", emoji=rank_info["emoji"], title=rank_info["title"]),
            body=t("rank_up_body", name=scholar["name"]),
            accent="gold"
        )
    else:
        notification_toast(
            t("current_rank_alt", emoji=rank_info["emoji"], title=rank_info["title"], xp=new_total_xp),
            kind="info"
        )

    rune_divider(t("your_reward"))

    rpg_card(
        title=f"🎖️ {reward['badge_name']}",
        body=reward["badge_description"],
        accent="gold",
        footer=reward["completion_message"]
    )

    rune_divider(t("wisdom_gained"))
    rpg_card(
        title=t("what_learned"),
        body=quest["learning_objective"],
        accent="arcane"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button(t("btn_new_dimension_results"),
                     use_container_width=True, type="primary", key="btn_new"):
            st.session_state.lesson_text   = ""
            st.session_state.pdf_name      = ""
            st.session_state.quest         = None
            st.session_state.chat_messages = []
            st.session_state.results_saved = False
            go_to("upload")
    with col2:
        if st.button(t("btn_return_academy"),
                     use_container_width=True, type="secondary", key="btn_home"):
            st.session_state.results_saved = False
            go_to("academy")
            
def page_archive():
    from backend.translations import t

    scholar    = st.session_state.scholar
    dimensions = get_scholar_dimensions(scholar["id"])
    _build_sidebar(scholar)

    page_header(t("archive_title_text"),
                subtitle=t("archive_subtitle", name=scholar['name']),
                icon="📚")

    if not dimensions:
        notification_toast(t("archive_empty"), kind="info")
    else:
        total_xp     = sum(d["xp_earned"] for d in dimensions)
        total_correct = sum(d["score"] for d in dimensions)
        total_q      = sum(d["total_questions"] for d in dimensions)

        # Summary stats
        col1, col2, col3 = st.columns(3)
        with col1:
            stat_pill(t("stat_dimensions"), str(len(dimensions)), "arcane")
        with col2:
            stat_pill(t("stat_total_xp"), str(total_xp), "gold")
        with col3:
            accuracy = int((total_correct / max(total_q, 1)) * 100)
            stat_pill(t("stat_accuracy"), f"{accuracy}%", "teal")

        rune_divider(t("conquered_dimensions"))

        for dim in dimensions:
            score_pct = int((dim["score"] / max(dim["total_questions"], 1)) * 100)
            accent = "gold" if score_pct == 100 else ("arcane" if score_pct >= 60 else "ember")
            rpg_card(
                title=dim["quest_title"],
                body=(
                    f'<span style="color:#5a4830;">📄</span> {dim["pdf_name"]}'
                    f'&nbsp;&nbsp;<span style="color:#3d1880;">·</span>&nbsp;&nbsp;'
                    f'<span style="color:#5a4830;">🌀</span> {dim["subject"]}'
                    f'<br>'
                    f'<span style="color:#7b2fff;">⚡</span> +{dim["xp_earned"]} XP'
                    f'&nbsp;&nbsp;<span style="color:#3d1880;">·</span>&nbsp;&nbsp;'
                    f'<span style="color:#c9a84c;">✅</span> {dim["score"]}/{dim["total_questions"]}'
                    f'&nbsp;&nbsp;<span style="color:#3d1880;">·</span>&nbsp;&nbsp;'
                    f'<span style="color:#5a4830;">{score_pct}%</span>'
                ),
                accent=accent,
                footer=dim["completed_at"][:10] if dim.get("completed_at") else "",
            )

    rune_divider()
    if st.button(t("btn_back_academy"),
                 use_container_width=True, type="secondary"):
        go_to("academy")

# ── Router ────────────────────────────────────────────────────
pages = {
    "login":       page_login,
    "quiz":        page_quiz,
    "academy":     page_academy,
    "upload":      page_upload,
    "chronicler":  page_chronicler,
    "generating":  page_generating,
    "quest_intro": page_quest_intro,
    "challenge":   page_challenge,
    "results":     page_results,
    "archive":     page_archive,
}

pages[st.session_state.page]()
