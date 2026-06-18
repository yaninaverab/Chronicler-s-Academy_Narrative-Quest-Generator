import streamlit as st
import json
import time
from backend.database import (
    init_db, create_scholar, get_scholar, name_exists,
    add_xp, get_rank_info, get_xp_for_next_rank,
    create_dimension, complete_dimension, get_scholar_dimensions,
    save_message, get_chat_history
)
from backend.streak_migration import apply_streak_migration
apply_streak_migration()
from backend.quest_generator import generate_quest, validate_quest
from ui.streak_ui import handle_login_streak, render_streak_panel, render_streak_badge
from backend.chronicler_prompts import build_chat_messages
from ui.theme import inject_theme, page_header, rpg_card, notification_toast

inject_theme()

# ── Init ──────────────────────────────────────────────────────
init_db()

st.set_page_config(
    page_title="The Chronicler's Academy",
    page_icon="🔮",
    layout="centered"
)

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
    xp = 50  # completion bonus
    xp += score * 30  # per correct answer
    if hints_used == 0:
        xp += 20  # no hints bonus
    if score == total:
        xp += 50  # perfect score bonus
    return xp

# ── Pages ─────────────────────────────────────────────────────

def page_login():
    #st.title("🔮 The Chronicler's Academy")
    page_header("The Academy", subtitle="Where legends are forged", icon="🏛")
    st.markdown("*Where knowledge becomes legend.*")
    st.divider()

    tab1, tab2 = st.tabs(["🧙 Returning Scholar", "✨ New Scholar"])

    with tab1:
        st.subheader("Welcome back, Scholar.")
        with st.form("login_form"):
            name = st.text_input("Your scholar name")
            pin = st.text_input("Your PIN", type="password", max_chars=4)
            submitted = st.form_submit_button("Enter the Academy ➡️",
                                              use_container_width=True)
            if submitted:
                if not name or not pin:
                    st.error("Please enter both your name and PIN.")
                else:
                    scholar = get_scholar(name, pin)
                    if scholar:
                        st.session_state.scholar = scholar
                        handle_login_streak(scholar)
                        go_to("academy")
                    else:
                        st.error("Scholar not found. Check your name and PIN.")

    with tab2:
        st.subheader("Begin your journey.")
        with st.form("register_form"):
            name = st.text_input("Choose your scholar name")
            pin = st.text_input("Choose a 4-digit PIN",
                                type="password", max_chars=4)
            pin2 = st.text_input("Confirm your PIN",
                                 type="password", max_chars=4)

            theme = st.selectbox("⚔️ Favorite theme", [
                "Space exploration", "Fantasy / Magic",
                "Mystery / Detective", "Sports",
                "Anime / Manga", "Superheroes",
                "Horror / Survival", "Historical adventure"
            ])
            difficulty = st.select_slider(
                "⚡ Difficulty",
                options=["Easy", "Medium", "Hard"]
            )
            interests = st.text_input(
                "❤️ Your interests",
                placeholder="e.g. soccer, anime, coding, music..."
            )
            want_quiz = st.checkbox(
                "🎯 Answer a few extra questions for better personalization"
            )
            submitted = st.form_submit_button("Create Scholar ✨",
                                              use_container_width=True)
            if submitted:
                if not name:
                    st.error("Please choose a scholar name.")
                elif not pin or len(pin) != 4 or not pin.isdigit():
                    st.error("PIN must be exactly 4 digits.")
                elif pin != pin2:
                    st.error("PINs don't match.")
                elif name_exists(name):
                    st.error("That name is already taken. Choose another.")
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
                        scholar_id = create_scholar(
                            data["name"], data["pin"],
                            data["theme"], data["difficulty"],
                            data["interests"]
                        )
                        scholar = get_scholar(data["name"], data["pin"])
                        st.session_state.scholar = scholar
                        go_to("academy")


def page_quiz():
    page_header("Personalization Quiz", subtitle="A few questions to shape your journey", icon="🎯")
    st.write("A few quick questions to make your journey more personal!")

    with st.form("quiz_form"):
        q1 = st.radio("When facing a challenge, you prefer to:", [
            "🧩 Solve a puzzle", "⚔️ Fight an enemy",
            "🗣️ Talk your way through", "🏃 Explore and discover"
        ])
        q2 = st.radio("Your ideal reward is:", [
            "🏆 A prestigious title", "✨ Powerful new abilities",
            "📖 Discovering a secret", "👥 Helping your team"
        ])
        q3 = st.radio("You prefer quests that are:", [
            "⚡ Fast and action-packed", "🧠 Deep and thought-provoking",
            "😂 Fun and lighthearted", "😱 Tense and mysterious"
        ])
        q4 = st.radio("Your hero style is:", [
            "🧙 Wise wizard", "🗡️ Brave warrior",
            "🕵️ Clever rogue", "💚 Supportive healer"
        ])
        submitted = st.form_submit_button("Begin my journey ➡️",
                                          use_container_width=True)
        if submitted:
            data = st.session_state._new_scholar_data
            interests_enriched = (
                f"{data['interests']}, play style: {q1}, "
                f"hero type: {q4}, quest style: {q3}"
            )
            scholar_id = create_scholar(
                data["name"], data["pin"],
                data["theme"], data["difficulty"],
                interests_enriched,
                play_style=q1, hero_type=q4,
                quest_style=q3, reward_preference=q2
            )
            scholar = get_scholar(data["name"], data["pin"])
            st.session_state.scholar = scholar
            go_to("academy")


def page_academy():
    scholar = st.session_state.scholar
    rank_info = get_rank_info(scholar["rank"])
    next_xp = get_xp_for_next_rank(scholar["rank"])
    dimensions = get_scholar_dimensions(scholar["id"])
    
    page_header("The Chronicler's Academy", subtitle=f"Welcome back, {scholar['name']}", icon=rank_info["emoji"])

    # Sidebar compact badge
    with st.sidebar:
        render_streak_badge(scholar)

    # Main panel (place near top of page)
    render_streak_panel(scholar)

    # XP Progress bar (now themed)
    from ui.theme import xp_bar
    if next_xp:
        xp_bar(
            current_xp=scholar["total_xp"],
            next_threshold=next_xp,
            rank_title=rank_info["title"],
            rank_num=scholar["rank"],
        )
    else:
        from ui.theme import notification_toast
        notification_toast("Maximum rank achieved — Chrono-Legend!", kind="success")

    st.divider()

    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📜 Enter a new Dimension",
                     use_container_width=True, type="primary"):
            st.session_state.lesson_text = ""
            st.session_state.pdf_name = ""
            st.session_state.quest = None
            st.session_state.chat_messages = []
            go_to("upload")
    with col2:
        if st.button("📚 Academy Archive",
                     use_container_width=True):
            go_to("archive")

    st.divider()

    # Recent dimensions
    if dimensions:
        st.markdown("### 🌀 Recent Dimensions")
        for dim in dimensions[:3]:
            rpg_card(
                title=dim["quest_title"],
                body=f"📄 {dim['pdf_name']}<br>⚡ +{dim['xp_earned']} XP &nbsp;&nbsp; ✅ {dim['score']}/{dim['total_questions']}",
                accent="arcane",
            )
    else:
        from ui.theme import notification_toast
        notification_toast("No dimensions explored yet. Begin your first journey!", kind="info")
        
    # Logout
    st.divider()
    if st.button("🚪 Leave Academy", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


def page_upload():
    scholar = st.session_state.scholar
    page_header("A New Dimension Awaits", subtitle="The Chronicler senses a lost tome from another realm", icon="📜")
    st.divider()

    tab1, tab2 = st.tabs(["📄 Upload PDF", "✏️ Paste text"])

    with tab1:
        uploaded = st.file_uploader("Upload your lesson PDF", type="pdf")
        if uploaded:
            import fitz
            pdf = fitz.open(stream=uploaded.read(), filetype="pdf")
            text = "".join(page.get_text() for page in pdf)
            st.session_state.lesson_text = text
            st.session_state.pdf_name = uploaded.name
            st.success(f"✅ Tome received! ({len(text)} characters)")
            st.text_area("Preview:", text[:400] + "...",
                         height=120, disabled=True)

    with tab2:
        pasted = st.text_area(
            "Paste your lesson content:",
            height=250,
            placeholder="Paste notes, textbook content, anything..."
        )
        if pasted:
            st.session_state.lesson_text = pasted
            st.session_state.pdf_name = "Manual entry"

    st.divider()

    if st.session_state.lesson_text:
        if st.button("🧙 Consult The Chronicler first",
                     use_container_width=True):
            go_to("chronicler")

        if st.button("⚔️ Generate Quest directly",
                     use_container_width=True, type="primary"):
            go_to("generating")

    if st.button("🏛️ Back to Academy", use_container_width=True):
        go_to("academy")


def page_chronicler():
    scholar = st.session_state.scholar
    st.title("🧙 The Chronicler Speaks")

    # Get rank title for personalization (matches your get_rank_info pattern)
    rank_info = get_rank_info(scholar["rank"])

    # Display chat history
    for msg in st.session_state.chat_messages:
        role = msg["role"]
        avatar = "🧙" if role == "assistant" else "🎓"
        with st.chat_message(role, avatar=avatar):
            st.write(msg["content"])

    # Chat input
    user_input = st.chat_input("Ask The Chronicler...")

    if user_input:
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input
        })

        from groq import Groq
        import os
        from dotenv import load_dotenv
        load_dotenv()

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        from backend.chronicler_prompts import build_chat_messages

        system_prompt, chat_msgs = build_chat_messages(
            scholar=scholar,
            history=st.session_state.chat_messages,
            new_message=user_input,
            rank_title=rank_info["title"],
            lesson_text=st.session_state.lesson_text,
        )

        messages = [{"role": "system", "content": system_prompt}] + chat_msgs

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.85,
            max_tokens=600,
        )

        reply = response.choices[0].message.content
        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": reply
        })
        st.rerun()

    st.divider()
    if st.button("⚔️ I'm ready — Generate my Quest!",
                 use_container_width=True, type="primary"):
        go_to("generating")

    if st.button("📜 Back to upload", use_container_width=True):
        go_to("upload")

def page_generating():
    st.title("⚔️ Entering the Dimension...")
    st.markdown("*The Chronicler weaves your quest from the ancient tome...*")

    with st.spinner("🔮 Crafting your personalized quest..."):
        try:
            scholar = st.session_state.scholar
            profile = {
                "name": scholar["name"],
                "theme": scholar["theme"],
                "difficulty": scholar["difficulty"],
                "interests": scholar["interests"],
            }
            quest = generate_quest(profile, st.session_state.lesson_text)

            if validate_quest(quest):
                st.session_state.quest = quest
                st.session_state.current_challenge = 0
                st.session_state.score = 0
                st.session_state.hints_used = 0
                st.session_state.answer_submitted = False

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
                st.error("Quest validation failed. Please try again.")
                time.sleep(2)
                go_to("upload")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            if st.button("Try again"):
                go_to("upload")


def page_quest_intro():
    quest = st.session_state.quest
    from ui.theme import quest_scroll, notification_toast

    quest_scroll(
        title=quest["quest_title"],
        topic=quest["theme"],
        difficulty=st.session_state.scholar.get("difficulty", "medium").lower(),
        num_questions=len(quest["challenges"]),
    )

    notification_toast(quest["story_intro"], kind="info")
    st.divider()

    st.markdown(f"### 🎯 Your Mission")
    st.write(quest["learning_objective"])
    st.divider()

    st.markdown(f"### 🗣️ {quest['npc_name']} says:")
    st.markdown(f"*\"{quest['npc_dialogue']}\"*")
    st.divider()

    st.markdown("### 📋 Quest Objectives")
    for step in quest["quest_steps"]:
        st.markdown(
            f"**{step['step_number']}.** {step['title']} "
            f"— {step['description']}"
        )

    st.divider()
    if st.button("⚔️ Begin the Trials!",
                 use_container_width=True, type="primary"):
        st.session_state.current_challenge = 1
        go_to("challenge")


def page_challenge():
    quest = st.session_state.quest
    total = len(quest["challenges"])
    current = st.session_state.current_challenge

    if current > total:
        go_to("results")
        return

    challenge = quest["challenges"][current - 1]

    st.title(f"⚔️ Trial {current} of {total}")
    print(repr(page_header.__module__))
    st.progress(current / total, text=f"Challenge {current} of {total}")
    st.divider()

    with st.container():
        st.markdown(f"### ❓ {challenge['question']}")

        answer = st.radio(
            "Choose your answer:",
            challenge["options"],
            key=f"challenge_{current}",
            disabled=st.session_state.answer_submitted,
        )

    col1, col2 = st.columns(2)

    # ── Not yet submitted: show Submit + Hint ──────────────────────────
    if not st.session_state.answer_submitted:
        with col1:
            if st.button("✅ Submit", use_container_width=True, type="primary"):
                correct = answer == challenge["correct_answer"]
                st.session_state.last_answer_correct = correct
                st.session_state.answer_submitted = True
                if correct:
                    st.session_state.score += 1
                st.rerun()

        with col2:
            if st.button("💡 Hint", use_container_width=True):
                st.warning(f"💡 {challenge['hint']}")
                st.session_state.hints_used += 1

    # ── Already submitted: show feedback + Next button ─────────────────
    else:
        if st.session_state.last_answer_correct:
            notification_toast(challenge["feedback_correct"], kind="success")
        else:
            notification_toast(challenge["feedback_incorrect"], kind="danger")
            notification_toast(f"Correct answer: {challenge['correct_answer']}", kind="info")

        if st.button("➡️ Next Trial", use_container_width=True, type="primary"):
            st.session_state.current_challenge += 1
            st.session_state.answer_submitted = False
            st.session_state.last_answer_correct = None
            if st.session_state.current_challenge > total:
                go_to("results")
            else:
                st.rerun()

def page_results():
    quest = st.session_state.quest
    scholar = st.session_state.scholar
    score = st.session_state.score
    total = len(quest["challenges"])
    hints = st.session_state.hints_used
    xp_earned = calculate_xp(score, total, hints)

    # Save to database
    complete_dimension(
        st.session_state.dimension_id,
        score, total, xp_earned, hints
    )
    new_total_xp, new_rank = add_xp(scholar["id"], xp_earned)

    # Update session scholar
    st.session_state.scholar["total_xp"] = new_total_xp
    st.session_state.scholar["rank"] = new_rank

    rank_info = get_rank_info(new_rank)
    old_rank = get_rank_info(scholar["rank"])

    st.balloons()
    page_header("Dimension Conquered!", subtitle=f"Well done, {scholar['name']}!", icon="🏆")

    from ui.theme import stat_pill
    col1, col2, col3 = st.columns(3)
    with col1:
        stat_pill("Score", f"{score}/{total}", "gold")
    with col2:
        stat_pill("XP Earned", f"+{xp_earned}", "arcane")
    with col3:
        stat_pill("Hints Used", str(hints), "teal")

    st.divider()

    # Rank up notification
    if new_rank > scholar["rank"]:
        st.success(
            f"🎉 RANK UP! You are now a "
            f"**{rank_info['emoji']} {rank_info['title']}**!"
        )
    else:
        st.info(
            f"{rank_info['emoji']} Current Rank: "
            f"**{rank_info['title']}** — {new_total_xp} XP total"
        )

    st.divider()

    reward = quest["reward"]
    st.markdown(f"### 🎖️ Badge: **{reward['badge_name']}**")
    st.write(reward["badge_description"])
    st.success(reward["completion_message"])

    st.divider()
    st.markdown("### 📚 What you learned")
    st.write(quest["learning_objective"])

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌀 New Dimension",
                     use_container_width=True, type="primary"):
            st.session_state.lesson_text = ""
            st.session_state.pdf_name = ""
            st.session_state.quest = None
            st.session_state.chat_messages = []
            go_to("upload")
    with col2:
        if st.button("🏛️ Return to Academy",
                     use_container_width=True):
            go_to("academy")


def page_archive():
    scholar = st.session_state.scholar
    dimensions = get_scholar_dimensions(scholar["id"])

    page_header("Academy Archive", subtitle=f"All dimensions conquered by {scholar['name']}", icon="📚")

    if not dimensions:
        from ui.theme import notification_toast
        notification_toast("No dimensions conquered yet. Begin your journey!", kind="info")
    else:
        for dim in dimensions:
            rpg_card(
                title=dim["quest_title"],
                body=f"📄 {dim['pdf_name']} &nbsp;·&nbsp; 🌀 {dim['subject']}<br>⚡ +{dim['xp_earned']} XP &nbsp;&nbsp; ✅ {dim['score']}/{dim['total_questions']}",
                accent="gold",
            )

    st.divider()
    if st.button("🏛️ Back to Academy", use_container_width=True):
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