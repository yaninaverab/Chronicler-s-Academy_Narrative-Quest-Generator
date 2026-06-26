from groq import Groq
import json
import os
from dotenv import load_dotenv
from backend.fallback_quest import get_fallback_quest
from backend.difficulty_prompts import build_quest_prompt

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_quest(student_profile: dict, lesson_text: str) -> dict:
    try:
        prompt = build_quest_prompt(student_profile, lesson_text)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an educational game designer. You always respond with valid JSON only, no markdown, no extra text."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2000,
        )

        raw_text = response.choices[0].message.content.strip()

        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]

        try:
            quest_data = json.loads(raw_text)
            return quest_data
        except json.JSONDecodeError:
            print("AI returned invalid JSON — using fallback quest")
            return get_fallback_quest()

    except Exception as e:
        print(f"Quest generation failed: {e} — using fallback quest")
        return get_fallback_quest()

def validate_quest(quest: dict) -> bool:
    """
    Basic validation to make sure the quest has all required fields.
    Protects against broken AI output crashing the app.
    """
    required_fields = [
        "quest_title", "theme", "story_intro", "learning_objective",
        "npc_name", "npc_dialogue", "quest_steps", "challenges", "reward"
    ]

    for field in required_fields:
        if field not in quest:
            print(f"Missing field: {field}")
            return False

    if len(quest["challenges"]) < 2:
        print("Not enough challenges generated")
        return False

    return True