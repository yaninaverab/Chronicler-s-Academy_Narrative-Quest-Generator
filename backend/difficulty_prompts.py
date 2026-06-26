"""
difficulty_prompts.py — Sharper difficulty prompting for quest generation.
Matches the REAL quest schema from quest_generator.py:
  quest_title, theme, story_intro, learning_objective,
  npc_name, npc_dialogue, quest_steps, challenges, reward

Usage:
    from backend.difficulty_prompts import build_quest_prompt
"""

from typing import Literal

DifficultyLevel = Literal["Easy", "Medium", "Hard"]

# ── Difficulty config ─────────────────────────────────────────────────────────
# NOTE: keys match your select_slider options exactly: "Easy" / "Medium" / "Hard"
DIFFICULTY_CONFIG = {
    "Easy": {
        "bloom_levels": ["remember", "understand"],
        "question_rules": [
            "Ask about definitions, basic facts, and direct recall from the lesson.",
            "Use clear, unambiguous language.",
            "Wrong options should be clearly wrong to someone who read the lesson.",
            "No trick questions or edge cases.",
        ],
        "wrong_answer_rule": "Wrong options should be plausible but clearly distinguishable from the correct answer.",
        "num_challenges": 3,
    },
    "Medium": {
        "bloom_levels": ["apply", "analyze"],
        "question_rules": [
            "Ask the student to apply concepts from the lesson to a small scenario, not just recall them.",
            "At least one question should involve 'why' or 'how', not just 'what'.",
            "Wrong options should be subtly wrong — requiring real understanding of the lesson to eliminate.",
        ],
        "wrong_answer_rule": "Wrong options should represent common misconceptions about the lesson content.",
        "num_challenges": 4,
    },
    "Hard": {
        "bloom_levels": ["evaluate", "synthesize"],
        "question_rules": [
            "Questions must require critical thinking — no answer should be immediately obvious from skimming.",
            "Include at least one question about a limitation, exception, or edge case from the lesson.",
            "Wrong options must be sophisticated — a student who half-read the lesson could easily pick them.",
            "Avoid 'all of the above' or 'none of the above' options.",
        ],
        "wrong_answer_rule": "Wrong options must be defensible at first glance — only real understanding of the lesson eliminates them.",
        "num_challenges": 5,
    },
}


# ── Main quest generation prompt ──────────────────────────────────────────────
def build_quest_prompt(student_profile: dict, lesson_text: str) -> str:
    """
    Builds the full quest generation prompt for Groq, matching the EXACT
    JSON schema your app already expects (quest_steps, challenges, reward).

    Drop-in replacement for the inline prompt block
    currently in quest_generator.py's generate_quest().
    """
    difficulty = student_profile.get("difficulty", "Medium")
    cfg = DIFFICULTY_CONFIG.get(difficulty, DIFFICULTY_CONFIG["Medium"])

    rules_block = "\n".join(f"- {r}" for r in cfg["question_rules"])
    bloom_block = ", ".join(cfg["bloom_levels"])
    num_challenges = cfg["num_challenges"]

    return f"""You are an expert educational game designer.
Your job is to transform a lesson into a personalized RPG quest for a student.


STUDENT PROFILE:
- Name: {student_profile['name']}
- Favorite theme: {student_profile['theme']}
- Difficulty: {difficulty}
f"- Weave the student's interests ({student_profile['interests']}) into scenario-based questions where possible.",

LESSON CONTENT:
{lesson_text}

DIFFICULTY TARGET: {difficulty} (Bloom's levels: {bloom_block})

CHALLENGE RULES — follow strictly for {difficulty} difficulty:
{rules_block}
- {cfg['wrong_answer_rule']}

INSTRUCTIONS:
- Create an RPG quest that teaches the EXACT concepts from the lesson
- Personalize the story, characters, and setting using the student's theme and interests
- Never invent facts — every challenge must come directly from the lesson content
- Keep language appropriate for a student
- Generate EXACTLY {num_challenges} challenges (not more, not fewer)
- The quest must be completable in 5-10 minutes

Return ONLY a valid JSON object with this exact structure, no extra text, no markdown:
{{
    "quest_title": "string",
    "theme": "string",
    "story_intro": "string (2-3 sentences setting the scene)",
    "learning_objective": "string (what the student will learn)",
    "npc_name": "string (the guide character name)",
    "npc_dialogue": "string (what the NPC says to introduce the quest)",
    "quest_steps": [
        {{"step_number": 1, "title": "string", "description": "string"}},
        {{"step_number": 2, "title": "string", "description": "string"}},
        {{"step_number": 3, "title": "string", "description": "string"}}
    ],
    "challenges": [
        {{
            "question": "string",
            "options": ["string", "string", "string", "string"],
            "correct_answer": "string",
            "hint": "string",
            "feedback_correct": "string",
            "feedback_incorrect": "string"
        }}
    ],
    "reward": {{
        "xp": 100,
        "badge_name": "string",
        "badge_description": "string",
        "completion_message": "string"
    }}
}}

Remember: generate exactly {num_challenges} challenge objects in the "challenges" array, each following the difficulty rules above.
"""