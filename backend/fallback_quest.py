"""
fallback_quest.py — Localized fallback quest for Chronicler's Academy.
Mirrors the language-lookup pattern used by t() in translations.py.

Usage:
    from backend.fallback_quest import get_fallback_quest

    quest = get_fallback_quest()   # reads st.session_state.language
"""

import streamlit as st

# ── English (original) ───────────────────────────────────────────────────
FALLBACK_QUEST_EN = {
    "quest_title": "The Syntax Scrolls of the Forgotten Archive",
    "theme": "Fantasy / Magic",
    "story_intro": (
        "Deep within the Chronicler's Archive, an ancient scroll "
        "has been discovered containing the fundamental laws of "
        "Python — the language of digital magic. The scroll is "
        "fading fast. You must absorb its knowledge before it "
        "disappears forever."
    ),
    "learning_objective": (
        "Understand Python variables: how to create them, "
        "naming rules, data types, and how to change their values."
    ),
    "npc_name": "Archivus",
    "npc_dialogue": (
        "Scholar! The scroll weakens by the second. "
        "Variables are the foundation of all Python magic — "
        "named containers that store the values powering our spells. "
        "Prove you understand them and the Archive shall reward you!"
    ),
    "quest_steps": [
        {
            "step_number": 1,
            "title": "Learn the Naming Laws",
            "description": (
                "Discover the sacred rules for naming "
                "variables in Python."
            )
        },
        {
            "step_number": 2,
            "title": "Master the Data Crystals",
            "description": (
                "Identify the four types of data a "
                "variable can store."
            )
        },
        {
            "step_number": 3,
            "title": "Seal the Knowledge",
            "description": (
                "Prove you can create and change "
                "variables correctly."
            )
        }
    ],
    "challenges": [
        {
            "question": (
                "Which of these is a valid Python variable name?"
            ),
            "options": [
                "2nd_spell",
                "my_spell",
                "my spell",
                "my-spell"
            ],
            "correct_answer": "my_spell",
            "hint": (
                "Variable names cannot start with numbers "
                "or contain spaces and hyphens."
            ),
            "feedback_correct": (
                "Correct! Underscores are the proper way "
                "to separate words in variable names."
            ),
            "feedback_incorrect": (
                "Not quite. Remember: no spaces, no hyphens, "
                "cannot start with a number."
            )
        },
        {
            "question": (
                "What data type would you use to store "
                "the message 'Hello Scholar'?"
            ),
            "options": [
                "Integer",
                "Float",
                "String",
                "Boolean"
            ],
            "correct_answer": "String",
            "hint": (
                "Text values are always stored in "
                "a specific type meant for characters."
            ),
            "feedback_correct": (
                "Excellent! Strings store text values, "
                "always wrapped in quotes."
            ),
            "feedback_incorrect": (
                "Not quite. Text is stored as a String, "
                "wrapped in quotes like 'Hello Scholar'."
            )
        },
        {
            "question": (
                "What happens when you run: "
                "score = 10 followed by score = 20?"
            ),
            "options": [
                "Both values are stored",
                "An error occurs",
                "score becomes 30",
                "score is now 20"
            ],
            "correct_answer": "score is now 20",
            "hint": (
                "Variables can only hold one value "
                "at a time. The new value replaces the old."
            ),
            "feedback_correct": (
                "Perfect! Variables can be reassigned "
                "anytime. The new value always replaces the old."
            ),
            "feedback_incorrect": (
                "Remember — a variable holds one value. "
                "Assigning a new value replaces the previous one."
            )
        }
    ],
    "reward": {
        "xp": 100,
        "badge_name": "Keeper of the Syntax Scrolls",
        "badge_description": (
            "Awarded to scholars who mastered Python variables "
            "under pressure in the Forgotten Archive."
        ),
        "completion_message": (
            "The scroll is saved! You have proven your mastery "
            "of Python variables. The Chronicler is proud, Scholar."
        )
    }
}

# ── Spanish ──────────────────────────────────────────────────────────────
# "Scholar" / "Chronicler" left untranslated to match the convention already
# used throughout translations.py (e.g. tab_returning, welcome_back).
FALLBACK_QUEST_ES = {
    "quest_title": "Los Pergaminos de Sintaxis del Archivo Olvidado",
    "theme": "Fantasy / Magic",  # stored value — used as-is by Groq prompts, not displayed directly
    "story_intro": (
        "En las profundidades del Archivo del Chronicler, se ha "
        "descubierto un pergamino antiguo que contiene las leyes "
        "fundamentales de Python — el lenguaje de la magia digital. "
        "El pergamino se desvanece rápidamente. Debes absorber su "
        "conocimiento antes de que desaparezca para siempre."
    ),
    "learning_objective": (
        "Comprender las variables de Python: cómo crearlas, "
        "las reglas de nomenclatura, los tipos de datos y cómo "
        "cambiar sus valores."
    ),
    "npc_name": "Archivus",
    "npc_dialogue": (
        "¡Scholar! El pergamino se debilita a cada segundo. "
        "Las variables son el fundamento de toda la magia de Python — "
        "contenedores nombrados que almacenan los valores que dan "
        "poder a nuestros hechizos. ¡Demuestra que las comprendes y "
        "el Archivo te recompensará!"
    ),
    "quest_steps": [
        {
            "step_number": 1,
            "title": "Aprende las Leyes de Nomenclatura",
            "description": (
                "Descubre las reglas sagradas para nombrar "
                "variables en Python."
            )
        },
        {
            "step_number": 2,
            "title": "Domina los Cristales de Datos",
            "description": (
                "Identifica los cuatro tipos de datos que "
                "puede almacenar una variable."
            )
        },
        {
            "step_number": 3,
            "title": "Sella el Conocimiento",
            "description": (
                "Demuestra que puedes crear y cambiar "
                "variables correctamente."
            )
        }
    ],
    "challenges": [
        {
            "question": (
                "¿Cuál de estos es un nombre de variable "
                "válido en Python?"
            ),
            "options": [
                "2do_hechizo",
                "mi_hechizo",
                "mi hechizo",
                "mi-hechizo"
            ],
            "correct_answer": "mi_hechizo",
            "hint": (
                "Los nombres de variables no pueden empezar con "
                "números ni contener espacios o guiones."
            ),
            "feedback_correct": (
                "¡Correcto! Los guiones bajos son la forma correcta "
                "de separar palabras en nombres de variables."
            ),
            "feedback_incorrect": (
                "No del todo. Recuerda: sin espacios, sin guiones, "
                "no puede empezar con un número."
            )
        },
        {
            "question": (
                "¿Qué tipo de dato usarías para almacenar "
                "el mensaje 'Hola Scholar'?"
            ),
            "options": [
                "Entero",
                "Flotante",
                "Cadena",
                "Booleano"
            ],
            "correct_answer": "Cadena",
            "hint": (
                "Los valores de texto siempre se almacenan en "
                "un tipo específico para caracteres."
            ),
            "feedback_correct": (
                "¡Excelente! Las cadenas almacenan valores de texto, "
                "siempre entre comillas."
            ),
            "feedback_incorrect": (
                "No del todo. El texto se almacena como una Cadena, "
                "entre comillas como 'Hola Scholar'."
            )
        },
        {
            "question": (
                "¿Qué sucede al ejecutar: "
                "puntaje = 10 seguido de puntaje = 20?"
            ),
            "options": [
                "Se almacenan ambos valores",
                "Ocurre un error",
                "puntaje se convierte en 30",
                "puntaje ahora es 20"
            ],
            "correct_answer": "puntaje ahora es 20",
            "hint": (
                "Las variables solo pueden contener un valor a la "
                "vez. El nuevo valor reemplaza al anterior."
            ),
            "feedback_correct": (
                "¡Perfecto! Las variables se pueden reasignar en "
                "cualquier momento. El nuevo valor siempre reemplaza al anterior."
            ),
            "feedback_incorrect": (
                "Recuerda — una variable contiene un solo valor. "
                "Asignar un nuevo valor reemplaza al anterior."
            )
        }
    ],
    "reward": {
        "xp": 100,
        "badge_name": "Guardián de los Pergaminos de Sintaxis",
        "badge_description": (
            "Otorgada a los scholars que dominaron las variables "
            "de Python bajo presión en el Archivo Olvidado."
        ),
        "completion_message": (
            "¡El pergamino se ha salvado! Has demostrado tu dominio "
            "de las variables de Python. El Chronicler está orgulloso, Scholar."
        )
    }
}


def get_fallback_quest() -> dict:
    """
    Returns the fallback quest in the current session language.
    Falls back to Spanish if language isn't set, mirroring t()'s default
    in translations.py.
    """
    lang = st.session_state.get("language", "es")
    return FALLBACK_QUEST_ES if lang == "es" else FALLBACK_QUEST_EN