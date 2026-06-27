"""
translations.py — UI string dictionary for Chronicler's Academy.
Supports English ("en") and Spanish ("es").

Usage:
    from backend.translations import t

    # In session state, store the chosen language:
    st.session_state.language = "es"  # or "en"

    # Then anywhere in app.py:
    st.title(t("academy_title"))
    st.button(t("btn_enter_academy"))
"""

import streamlit as st

TRANSLATIONS = {
    "es": {
        # ── Login page ──────────────────────────────────────────────
        "academy_name": "The Academy",
        "academy_name_line1": "La Academia del",
        "academy_name_line2": "CHRONICLER",
        "academy_tagline": "Donde las leyendas se forjan",
        "academy_subtitle": "Donde el conocimiento se convierte en leyenda",
        "tab_returning": "🧙 Scholar Existente",
        "tab_new": "✨ Nuevo Scholar",
        "welcome_back": "Bienvenido de nuevo, Scholar.",
        "begin_journey": "Comienza tu viaje.",
        "label_scholar_name": "Tu nombre de scholar",
        "label_pin": "Tu PIN",
        "label_choose_name": "Elige tu nombre de scholar",
        "label_choose_pin": "Elige un PIN de 4 dígitos",
        "label_confirm_pin": "Confirma tu PIN",
        "btn_enter_academy": "Entrar a la Academia ➡️",
        "btn_create_scholar": "Crear Scholar ✨",
        "error_name_pin_required": "Por favor ingresa tu nombre y PIN.",
        "error_scholar_not_found": "Scholar no encontrado. Verifica tu nombre y PIN.",
        "error_choose_name": "Por favor elige un nombre de scholar.",
        "error_pin_length": "El PIN debe tener exactamente 4 dígitos.",
        "error_pin_mismatch": "Los PINs no coinciden.",
        "error_name_taken": "Ese nombre ya está en uso. Elige otro.",

        # ── Registration ────────────────────────────────────────────
        "label_theme": "⚔️ Tema favorito",
        "label_difficulty": "⚡ Dificultad",
        "label_interests": "❤️ Tus intereses",
        "placeholder_interests": "ej. fútbol, anime, programación, música...",
        "label_want_quiz": "🎯 Responder algunas preguntas extra para mejor personalización",

        # ── Academy page ────────────────────────────────────────────
        "academy_page_title": "🏛️ La Academia del Chronicler",
        "academy_page_title_text": "La Academia del Chronicler",
        "welcome_scholar": "Bienvenido de nuevo, **{name}**",
        "welcome_back_name": "Bienvenido de nuevo, {name}",
        "btn_new_dimension": "📜 Entrar a una nueva Dimensión",
        "btn_new_dimension_text": "Entrar a una nueva Dimensión",
        "btn_archive": "📚 Archivo de la Academia",
        "recent_dimensions": "🌀 Dimensiones Recientes",
        "no_dimensions": "🌀 Aún no has explorado dimensiones. ¡Comienza tu primer viaje!",
        "no_dimensions_long": "Aún no has explorado dimensiones. El Archivo espera tu primer tomo.",
        "btn_leave_academy": "🚪 Salir de la Academia",
        "max_rank_achieved": "⚡ ¡Rango máximo alcanzado — Chrono-Legend!",
        "xp_to_next_rank": "⚡ {current} / {next} XP para el siguiente rango",
        "rune_divider_begin_journey": "Comienza tu viaje",
        "rune_divider_recent_dimensions": "Dimensiones Recientes",

        # ── Upload page ─────────────────────────────────────────────
        "upload_title": "📜 Una Nueva Dimensión Aguarda",
        "upload_title_text": "Se Requiere un Tomo",
        "upload_subtitle": "El Chronicler percibe un tomo perdido de otro reino...",
        "upload_subtitle_alt": "El Chronicler percibe conocimiento inexplorado cerca",
        "tab_upload_pdf": "📄 Subir PDF",
        "tab_paste_text": "✏️ Pegar texto",
        "tab_inscribe_text": "✏️ Inscribir Texto",
        "label_upload_pdf": "Sube tu PDF de lección",
        "label_drop_tome": "Coloca aquí el tomo de tu lección",
        "label_paste_content": "Pega el contenido de tu lección:",
        "label_inscribe_lesson": "Inscribe tu lección:",
        "placeholder_paste": "Pega apuntes, contenido de libro, lo que sea...",
        "placeholder_inscribe": "Pega apuntes, fragmentos de libro, lo que merezca ser estudiado...",
        "tome_received": "✅ ¡Tomo recibido! ({chars} caracteres)",
        "tome_received_html": "Tomo recibido — <strong>{filename}</strong> ({chars} caracteres)",
        "manual_inscription": "Inscripción manual",
        "preview_tome": "📖 Vista previa del tomo",
        "btn_consult_chronicler": "🧙 Consultar al Chronicler primero",
        "btn_consult_chronicler_alt": "🧙 Consultar al Chronicler",
        "btn_generate_direct": "⚔️ Generar Misión directamente",
        "btn_generate_quest": "⚔️ Generar Misión",
        "btn_back_academy": "🏛️ Volver a la Academia",
        "upload_or_inscribe_prompt": "Sube un tomo o inscribe texto para continuar.",
        "difficulty_override_label": "⚡ Dificultad para esta misión",  


        # ── Chronicler page ─────────────────────────────────────────
        "chronicler_title": "🧙 El Chronicler Habla",
        "chronicler_title_text": "El Chronicler Habla",
        "chronicler_subtitle": "Pregúntame lo que quieras sobre este tomo antes de partir...",
        "chronicler_subtitle_alt": "Sabiduría ancestral, impaciencia apenas disimulada",
        "chat_placeholder": "Pregúntale al Chronicler...",
        "btn_ready_quest": "⚔️ Estoy listo — ¡Genera mi Misión!",
        "btn_generate_quest_alt": "⚔️ Generar mi Misión",
        "btn_back_upload": "📜 Volver a subir contenido",
        "btn_back_upload_alt": "📜 Volver a Subir",

        # ── Generating page ─────────────────────────────────────────
        "generating_title": "⚔️ Entrando a la Dimensión...",
        "generating_title_text": "Entrando a la Dimensión",
        "generating_subtitle": "El Chronicler teje tu misión a partir del tomo ancestral...",
        "generating_subtitle_alt": "El Chronicler teje tu misión a partir del tomo ancestral",
        "consulting_records": "Consultando los registros arcanos",
        "spinner_crafting": "🔮 Creando tu misión personalizada...",
        "error_quest_validation": "La validación de la misión falló. Intenta de nuevo.",
        "error_generic": "Algo salió mal: {error}",
        "btn_try_again": "Intentar de nuevo",
        "btn_try_again_alt": "🔄 Intentar de nuevo",

        # ── Quest intro page ─────────────────────────────────────────
        "your_mission": "🎯 Tu Misión",
        "learning_objective_title": "🎯 Objetivo de Aprendizaje",
        "mission_briefing": "Informe de la Misión",
        "quest_objectives": "📋 Objetivos de la Misión",
        "quest_objectives_text": "Objetivos de la Misión",
        "btn_begin_trials": "⚔️ ¡Comenzar las Pruebas!",
        "btn_begin_trials_alt": "⚔️ Comenzar las Pruebas",

        # ── Challenge page ──────────────────────────────────────────
        "trial_of": "⚔️ Prueba {current} de {total}",
        "challenge_of": "Desafío {current} de {total}",
        "choose_answer": "Elige tu respuesta:",
        "chroniclers_hint": "Pista del Chronicler",
        "btn_submit": "✅ Enviar",
        "btn_submit_answer": "✅ Enviar Respuesta",
        "btn_hint": "💡 Pista",
        "btn_next_trial": "➡️ Siguiente Prueba",
        "correct_answer_label": "Respuesta correcta: {answer}",
        "feedback_correct_prefix": "✦ ¡Correcto!",
        "feedback_incorrect_prefix": "✕ Incorrecto.",
        "feedback_correct_answer_html": "Respuesta correcta: <strong>{answer}</strong>",

        # ── Results page ─────────────────────────────────────────────
        "results_title": "🏆 ¡Dimensión Conquistada!",
        "well_done": "## ¡Bien hecho, {name}!",
        "metric_score": "Puntaje",
        "metric_xp_earned": "XP Ganado",
        "metric_hints": "Pistas Usadas",
        "rank_up": "🎉 ¡SUBISTE DE RANGO! Ahora eres un **{emoji} {title}**!",
        "rank_up_title": "🎉 SUBISTE DE RANGO — {emoji} {title}",
        "rank_up_body": "Has ascendido, {name}. El Chronicler reconoce tu crecimiento.",
        "current_rank": "{emoji} Rango Actual: **{title}** — {xp} XP total",
        "current_rank_alt": "{emoji} {title} — {xp} XP total",
        "badge_label": "🎖️ Insignia: **{badge}**",
        "what_learned": "📚 Lo que aprendiste",
        "your_reward": "Tu Recompensa",
        "wisdom_gained": "Sabiduría Adquirida",
        "btn_new_dimension_results": "🌀 Nueva Dimensión",
        "btn_return_academy": "🏛️ Volver a la Academia",

        # ── Archive page ─────────────────────────────────────────────
        "archive_title": "📚 Archivo de la Academia",
        "archive_title_text": "Archivo de la Academia",
        "archive_subtitle": "Todas las dimensiones conquistadas por {name}",
        "no_dimensions_archive": "Aún no se han conquistado dimensiones. ¡Comienza tu viaje!",
        "archive_empty": "El archivo está vacío. Aún no se ha conquistado ninguna dimensión.",
        "stat_dimensions": "Dimensiones",
        "stat_total_xp": "XP Total",
        "stat_accuracy": "Precisión",
        "conquered_dimensions": "Dimensiones Conquistadas",

        # ── Sidebar navigation ──────────────────────────────────────
        "sidebar_navigation": "Navegación",
        "nav_academy": "🏛️ Academia",
        "nav_new_dimension": "🌀 Nueva Dimensión",
        "nav_archive": "📚 Archivo",
        "nav_logout": "🚪 Salir de la Academia",

        # ── Language selector ───────────────────────────────────────
        "language_label": "🌐 Idioma",

        # ── Theme options (displayed translated, stored in English) ──
        "theme_Space Exploration": "Exploración Espacial",
        "theme_Fantasy / Magic": "Fantasía / Magia",
        "theme_Mystery / Detective": "Misterio / Detective",
        "theme_Sports": "Deportes",
        "theme_Anime / Manga": "Anime / Manga",
        "theme_Superheroes": "Superhéroes",
        "theme_Horror / Survival": "Horror / Supervivencia",
        "theme_Historical Adventure": "Aventura Histórica",

        # ── Difficulty options (displayed translated, stored in English) ──
        "difficulty_Easy": "Fácil",
        "difficulty_Medium": "Medio",
        "difficulty_Hard": "Difícil",

        # ── Quiz page ────────────────────────────────────────────────
        "quiz_title": "Rito de Personalización",
        "quiz_subtitle": "El Chronicler lee tu alma",
        "quiz_divider": "Responde con sinceridad",
        "quiz_q1": "Al enfrentar un desafío, prefieres:",
        "quiz_q1_opt1": "🧩 Resolver un acertijo",
        "quiz_q1_opt2": "⚔️ Luchar contra un enemigo",
        "quiz_q1_opt3": "🗣️ Hablar para resolverlo",
        "quiz_q1_opt4": "🏃 Explorar y descubrir",
        "quiz_q2": "Tu recompensa ideal es:",
        "quiz_q2_opt1": "🏆 Un título prestigioso",
        "quiz_q2_opt2": "✨ Nuevas habilidades poderosas",
        "quiz_q2_opt3": "📖 Descubrir un secreto",
        "quiz_q2_opt4": "👥 Ayudar a tu equipo",
        "quiz_q3": "Prefieres misiones que sean:",
        "quiz_q3_opt1": "⚡ Rápidas y llenas de acción",
        "quiz_q3_opt2": "🧠 Profundas y reflexivas",
        "quiz_q3_opt3": "😂 Divertidas y ligeras",
        "quiz_q3_opt4": "😱 Tensas y misteriosas",
        "quiz_q4": "Tu arquetipo de héroe es:",
        "quiz_q4_opt1": "🧙 Mago sabio",
        "quiz_q4_opt2": "🗡️ Guerrero valiente",
        "quiz_q4_opt3": "🕵️ Rebelde astuto",
        "quiz_q4_opt4": "💚 Sanador de apoyo",
        "btn_seal_path": "📜 Sellar mi Camino",

        # ── theme.py components ──────────────────────────────────────
        "rank_progress":            "Progreso de Rango",
        "xp_to_next":               "{xp} / {next}",
        "max_rank_display":         "MÁXIMO",
        "remaining_xp":             "{remaining} XP para subir de rango",
        "max_rank_reached":         "Chrono-Legend — Cima alcanzada",
        "streak_day_label":         "🔥 {streak} días de racha",
        "sidebar_xp_label":         "XP",
        "sidebar_streak_label":     "Racha",
        "sidebar_rank_label":       "Rango",
        "result_flawless":          "VICTORIA IMPECABLE",
        "result_conquered":         "DIMENSIÓN CONQUISTADA",
        "result_complete":          "PRUEBA COMPLETADA",
        "result_correct_label":     "Correctas",
        "result_xp_label":          "XP Ganado",
        "xp_to_next_rank_bar":      "{remaining} XP al siguiente rango",

                
        # ── streak_ui.py components ──────────────────────────────────
        "streak_day_count":      "Día {day} de Racha",
        "streak_day_frozen":     "Día {day} (congelada)",
        "streak_bonus_xp":       "+{xp} XP de bonus",
        "streak_keep_going":     "¡Sigue así, Scholar!",
        "streak_frozen_notice":  "❄️ Período de gracia activo — ¡inicia sesión mañana para mantener tu racha!",
        "streak_reset_notice":   "Tu racha se ha reiniciado. Comienza de nuevo, Scholar.",
        "streak_already_today":  "Ya iniciaste sesión hoy. Bien hecho.",
        "streak_milestone_xp":   "+{xp} XP otorgados!",
        "streak_badge_label":    "{streak} días de racha",
        "day_singular": "día",
        "day_plural":   "días",
        
        # ── Streak manager componenets ─────────────────────────────
        "milestone_ember_badge":     "Guardián de la Llama",
        "milestone_ember_title":     "La llama se enciende…",
        "milestone_week_badge":      "Guardián Semanal",
        "milestone_week_title":      "Siete días de devoción.",
        "milestone_fortnight_badge": "Forjado en Quincena",
        "milestone_fortnight_title": "Dos semanas — el archivo se inclina.",
        "milestone_eternal_badge":   "Chronicler Eterno",
        "milestone_eternal_title":   "Un mes ininterrumpido. Leyenda.",
    },

    "en": {
        # ── Login page ──────────────────────────────────────────────
        "academy_name": "The Academy",
        "academy_name_line1": "The Chronicler's",
        "academy_name_line2": "ACADEMY",
        "academy_tagline": "Where legends are forged",
        "academy_subtitle": "Where knowledge becomes legend",
        "tab_returning": "🧙 Returning Scholar",
        "tab_new": "✨ New Scholar",
        "welcome_back": "Welcome back, Scholar.",
        "begin_journey": "Begin your journey.",
        "label_scholar_name": "Your scholar name",
        "label_pin": "Your PIN",
        "label_choose_name": "Choose your scholar name",
        "label_choose_pin": "Choose a 4-digit PIN",
        "label_confirm_pin": "Confirm your PIN",
        "btn_enter_academy": "Enter the Academy ➡️",
        "btn_create_scholar": "Create Scholar ✨",
        "error_name_pin_required": "Please enter both your name and PIN.",
        "error_scholar_not_found": "Scholar not found. Check your name and PIN.",
        "error_choose_name": "Please choose a scholar name.",
        "error_pin_length": "PIN must be exactly 4 digits.",
        "error_pin_mismatch": "PINs don't match.",
        "error_name_taken": "That name is already taken. Choose another.",

        # ── Registration ────────────────────────────────────────────
        "label_theme": "⚔️ Favorite theme",
        "label_difficulty": "⚡ Difficulty",
        "label_interests": "❤️ Your interests",
        "placeholder_interests": "e.g. soccer, anime, coding, music...",
        "label_want_quiz": "🎯 Answer a few extra questions for better personalization",

        # ── Academy page ────────────────────────────────────────────
        "academy_page_title": "🏛️ The Chronicler's Academy",
        "academy_page_title_text": "The Chronicler's Academy",
        "welcome_scholar": "Welcome back, **{name}**",
        "welcome_back_name": "Welcome back, {name}",
        "btn_new_dimension": "📜 Enter a new Dimension",
        "btn_new_dimension_text": "Enter a New Dimension",
        "btn_archive": "📚 Academy Archive",
        "recent_dimensions": "🌀 Recent Dimensions",
        "no_dimensions": "🌀 No dimensions explored yet. Begin your first journey!",
        "no_dimensions_long": "No dimensions explored yet. The Archive awaits your first tome.",
        "btn_leave_academy": "🚪 Leave Academy",
        "max_rank_achieved": "⚡ Maximum rank achieved — Chrono-Legend!",
        "xp_to_next_rank": "⚡ {current} / {next} XP to next rank",
        "rune_divider_begin_journey": "Begin your journey",
        "rune_divider_recent_dimensions": "Recent Dimensions",

        # ── Upload page ─────────────────────────────────────────────
        "upload_title": "📜 A New Dimension Awaits",
        "upload_title_text": "A Tome is Required",
        "upload_subtitle": "The Chronicler senses a lost tome from another realm...",
        "upload_subtitle_alt": "The Chronicler senses uncharted knowledge nearby",
        "tab_upload_pdf": "📄 Upload PDF",
        "tab_paste_text": "✏️ Paste text",
        "tab_inscribe_text": "✏️ Inscribe Text",
        "label_upload_pdf": "Upload your lesson PDF",
        "label_drop_tome": "Drop your lesson tome here",
        "label_paste_content": "Paste your lesson content:",
        "label_inscribe_lesson": "Inscribe your lesson:",
        "placeholder_paste": "Paste notes, textbook content, anything...",
        "placeholder_inscribe": "Paste notes, textbook excerpts, anything worth studying...",
        "tome_received": "✅ Tome received! ({chars} characters)",
        "tome_received_html": "Tome received — <strong>{filename}</strong> ({chars} characters)",
        "manual_inscription": "Manual inscription",
        "preview_tome": "📖 Preview tome contents",
        "btn_consult_chronicler": "🧙 Consult The Chronicler first",
        "btn_consult_chronicler_alt": "🧙 Consult the Chronicler",
        "btn_generate_direct": "⚔️ Generate Quest directly",
        "btn_generate_quest": "⚔️ Generate Quest",
        "btn_back_academy": "🏛️ Back to Academy",
        "upload_or_inscribe_prompt": "Upload a tome or inscribe text to continue.",
        "difficulty_override_label": "⚡ Difficulty for this quest",   

        # ── Chronicler page ─────────────────────────────────────────
        "chronicler_title": "🧙 The Chronicler Speaks",
        "chronicler_title_text": "The Chronicler Speaks",
        "chronicler_subtitle": "Ask me anything about this tome before you venture forth...",
        "chronicler_subtitle_alt": "Ancient wisdom, barely concealed impatience",
        "chat_placeholder": "Ask The Chronicler...",
        "btn_ready_quest": "⚔️ I'm ready — Generate my Quest!",
        "btn_generate_quest_alt": "⚔️ Generate my Quest",
        "btn_back_upload": "📜 Back to upload",
        "btn_back_upload_alt": "📜 Back to Upload",

        # ── Generating page ─────────────────────────────────────────
        "generating_title": "⚔️ Entering the Dimension...",
        "generating_title_text": "Entering the Dimension",
        "generating_subtitle": "The Chronicler weaves your quest from the ancient tome...",
        "generating_subtitle_alt": "The Chronicler weaves your quest from the ancient tome",
        "consulting_records": "Consulting the arcane records",
        "spinner_crafting": "🔮 Crafting your personalized quest...",
        "error_quest_validation": "Quest validation failed. Please try again.",
        "error_generic": "Something went wrong: {error}",
        "btn_try_again": "Try again",
        "btn_try_again_alt": "🔄 Try again",

        # ── Quest intro page ─────────────────────────────────────────
        "your_mission": "🎯 Your Mission",
        "learning_objective_title": "🎯 Learning Objective",
        "mission_briefing": "Mission Briefing",
        "quest_objectives": "📋 Quest Objectives",
        "quest_objectives_text": "Quest Objectives",
        "btn_begin_trials": "⚔️ Begin the Trials!",
        "btn_begin_trials_alt": "⚔️ Begin the Trials",

        # ── Challenge page ──────────────────────────────────────────
        "trial_of": "⚔️ Trial {current} of {total}",
        "challenge_of": "Challenge {current} of {total}",
        "choose_answer": "Choose your answer:",
        "chroniclers_hint": "The Chronicler's Hint",
        "btn_submit": "✅ Submit",
        "btn_submit_answer": "✅ Submit Answer",
        "btn_hint": "💡 Hint",
        "btn_next_trial": "➡️ Next Trial",
        "correct_answer_label": "Correct answer: {answer}",
        "feedback_correct_prefix": "✦ Correct!",
        "feedback_incorrect_prefix": "✕ Incorrect.",
        "feedback_correct_answer_html": "Correct answer: <strong>{answer}</strong>",

        # ── Results page ─────────────────────────────────────────────
        "results_title": "🏆 Dimension Conquered!",
        "well_done": "## Well done, {name}!",
        "metric_score": "Score",
        "metric_xp_earned": "XP Earned",
        "metric_hints": "Hints Used",
        "rank_up": "🎉 RANK UP! You are now a **{emoji} {title}**!",
        "rank_up_title": "🎉 RANK UP — {emoji} {title}",
        "rank_up_body": "You have ascended, {name}. The Chronicler acknowledges your growth.",
        "current_rank": "{emoji} Current Rank: **{title}** — {xp} XP total",
        "current_rank_alt": "{emoji} {title} — {xp} XP total",
        "badge_label": "🎖️ Badge: **{badge}**",
        "what_learned": "📚 What you learned",
        "your_reward": "Your Reward",
        "wisdom_gained": "Wisdom Gained",
        "btn_new_dimension_results": "🌀 New Dimension",
        "btn_return_academy": "🏛️ Return to Academy",

        # ── Archive page ─────────────────────────────────────────────
        "archive_title": "📚 Academy Archive",
        "archive_title_text": "Academy Archive",
        "archive_subtitle": "All dimensions conquered by {name}",
        "no_dimensions_archive": "No dimensions conquered yet. Begin your journey!",
        "archive_empty": "The archive is empty. No dimensions have been conquered yet.",
        "stat_dimensions": "Dimensions",
        "stat_total_xp": "Total XP",
        "stat_accuracy": "Accuracy",
        "conquered_dimensions": "Conquered Dimensions",

        # ── Sidebar navigation ──────────────────────────────────────
        "sidebar_navigation": "Navigation",
        "nav_academy": "🏛️ Academy",
        "nav_new_dimension": "🌀 New Dimension",
        "nav_archive": "📚 Archive",
        "nav_logout": "🚪 Leave Academy",

        # ── Language selector ───────────────────────────────────────
        "language_label": "🌐 Language",

        # ── Theme options (identity mapping — already in English) ───
        "theme_Space Exploration": "Space Exploration",
        "theme_Fantasy / Magic": "Fantasy / Magic",
        "theme_Mystery / Detective": "Mystery / Detective",
        "theme_Sports": "Sports",
        "theme_Anime / Manga": "Anime / Manga",
        "theme_Superheroes": "Superheroes",
        "theme_Horror / Survival": "Horror / Survival",
        "theme_Historical Adventure": "Historical Adventure",

        # ── Difficulty options (identity mapping — already in English) ──
        "difficulty_Easy": "Easy",
        "difficulty_Medium": "Medium",
        "difficulty_Hard": "Hard",

    # ── theme.py components ──────────────────────────────────────
        "rank_progress":            "Rank Progress",
        "xp_to_next":               "{xp} / {next}",
        "max_rank_display":         "MAX",
        "remaining_xp":             "{remaining} XP to rank up",
        "max_rank_reached":         "Chrono-Legend — Peak reached",
        "streak_day_label":         "🔥 {streak}-day streak",
        "sidebar_xp_label":         "XP",
        "sidebar_streak_label":     "Streak",
        "sidebar_rank_label":       "Rank",
        "result_flawless":          "FLAWLESS VICTORY",
        "result_conquered":         "DIMENSION CONQUERED",
        "result_complete":          "TRIAL COMPLETE",
        "result_correct_label":     "Correct",
        "result_xp_label":          "XP Earned",
        "xp_to_next_rank_bar":      "{remaining} XP to next rank",

        # ── streak_ui.py components ──────────────────────────────────
        "streak_day_count":      "Day {day} Streak",
        "streak_day_frozen":     "Day {day} (frozen)",
        "streak_bonus_xp":       "+{xp} XP bonus",
        "streak_keep_going":     "Keep it up, Scholar!",
        "streak_frozen_notice":  "❄️ Grace period active — log in tomorrow to keep your streak!",
        "streak_reset_notice":   "Your streak has been reset. Begin anew, Scholar.",
        "streak_already_today":  "You've already logged in today. Well done.",
        "streak_milestone_xp":   "+{xp} XP awarded!",
        "streak_badge_label":    "{streak}-day streak",
        "day_singular": "day",
        "day_plural":   "days",
        
        # ── Quiz page ────────────────────────────────────────────────
        "quiz_title": "Personalization Rite",
        "quiz_subtitle": "The Chronicler reads your soul",
        "quiz_divider": "Answer truthfully",
        "quiz_q1": "When facing a challenge, you prefer to:",
        "quiz_q1_opt1": "🧩 Solve a puzzle",
        "quiz_q1_opt2": "⚔️ Fight an enemy",
        "quiz_q1_opt3": "🗣️ Talk your way through",
        "quiz_q1_opt4": "🏃 Explore and discover",
        "quiz_q2": "Your ideal reward is:",
        "quiz_q2_opt1": "🏆 A prestigious title",
        "quiz_q2_opt2": "✨ Powerful new abilities",
        "quiz_q2_opt3": "📖 Discovering a secret",
        "quiz_q2_opt4": "👥 Helping your team",
        "quiz_q3": "You prefer quests that are:",
        "quiz_q3_opt1": "⚡ Fast and action-packed",
        "quiz_q3_opt2": "🧠 Deep and thought-provoking",
        "quiz_q3_opt3": "😂 Fun and lighthearted",
        "quiz_q3_opt4": "😱 Tense and mysterious",
        "quiz_q4": "Your hero archetype is:",
        "quiz_q4_opt1": "🧙 Wise wizard",
        "quiz_q4_opt2": "🗡️ Brave warrior",
        "quiz_q4_opt3": "🕵️ Clever rogue",
        "quiz_q4_opt4": "💚 Supportive healer",
        "btn_seal_path": "📜 Seal my Path",
        
        # ── Streak manager componenets ─────────────────────────────
        "milestone_ember_badge":     "Ember Keeper",
        "milestone_ember_title":     "The flame ignites…",
        "milestone_week_badge":      "Week Warden",
        "milestone_week_title":      "Seven days of devotion.",
        "milestone_fortnight_badge": "Fortnight Forged",
        "milestone_fortnight_title": "Two weeks — the archive bows.",
        "milestone_eternal_badge":   "Eternal Chronicler",
        "milestone_eternal_title":   "A month unbroken. Legend.",
    },
}


def t(key: str, **kwargs) -> str:
    """
    Translate a UI string key into the current session language.
    Falls back to Spanish if language isn't set, falls back to the
    key itself if the key doesn't exist (so missing translations are
    visible/obvious instead of crashing).

    Usage:
        t("welcome_back")
        t("welcome_scholar", name=scholar["name"])
    """
    lang = st.session_state.get("language", "es")
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS["es"])
    text = lang_dict.get(key, key)

    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, IndexError):
            return text

    return text


# ── Theme / Difficulty option translation helpers ────────────────────────────
# These options are ALWAYS stored in English in the database (and used as-is
# in Groq prompts), but displayed translated in the UI dropdown/slider.

THEME_OPTIONS_EN = [
    "Space Exploration", "Fantasy / Magic",
    "Mystery / Detective", "Sports",
    "Anime / Manga", "Superheroes",
    "Horror / Survival", "Historical Adventure",
]

DIFFICULTY_OPTIONS_EN = ["Easy", "Medium", "Hard"]


def translated_theme_options() -> list:
    """Returns the theme options translated for display, in the same order as THEME_OPTIONS_EN."""
    return [t(f"theme_{opt}") for opt in THEME_OPTIONS_EN]


def translated_difficulty_options() -> list:
    """Returns the difficulty options translated for display, in the same order as DIFFICULTY_OPTIONS_EN."""
    return [t(f"difficulty_{opt}") for opt in DIFFICULTY_OPTIONS_EN]


def theme_display_to_english(displayed_value: str) -> str:
    """Converts a displayed (translated) theme value back to its English storage value."""
    translated = translated_theme_options()
    if displayed_value in translated:
        return THEME_OPTIONS_EN[translated.index(displayed_value)]
    return displayed_value  # fallback — already English or unrecognized


def difficulty_display_to_english(displayed_value: str) -> str:
    """Converts a displayed (translated) difficulty value back to its English storage value."""
    translated = translated_difficulty_options()
    if displayed_value in translated:
        return DIFFICULTY_OPTIONS_EN[translated.index(displayed_value)]
    return displayed_value  # fallback — already English or unrecognized


# ── Quiz option translation helpers ───────────────────────────────────────────
# Quiz answers are stored in English (play_style, hero_type, etc. feed into
# Chronicler prompts), but displayed translated as radio options.

QUIZ_OPTIONS_EN = {
    "q1": ["🧩 Solve a puzzle", "⚔️ Fight an enemy", "🗣️ Talk your way through", "🏃 Explore and discover"],
    "q2": ["🏆 A prestigious title", "✨ Powerful new abilities", "📖 Discovering a secret", "👥 Helping your team"],
    "q3": ["⚡ Fast and action-packed", "🧠 Deep and thought-provoking", "😂 Fun and lighthearted", "😱 Tense and mysterious"],
    "q4": ["🧙 Wise wizard", "🗡️ Brave warrior", "🕵️ Clever rogue", "💚 Supportive healer"],
}


def translated_quiz_options(question_key: str) -> list:
    """Returns translated options for a quiz question (q1-q4), same order as QUIZ_OPTIONS_EN."""
    return [t(f"quiz_{question_key}_opt{i+1}") for i in range(4)]


def quiz_display_to_english(question_key: str, displayed_value: str) -> str:
    """Converts a displayed (translated) quiz answer back to its English storage value."""
    translated = translated_quiz_options(question_key)
    english = QUIZ_OPTIONS_EN[question_key]
    if displayed_value in translated:
        return english[translated.index(displayed_value)]
    return displayed_value  # fallback