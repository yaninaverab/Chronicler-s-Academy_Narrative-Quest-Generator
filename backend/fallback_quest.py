FALLBACK_QUEST = {
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