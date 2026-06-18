from backend.quest_generator import generate_quest, validate_quest

# Sample student profile
student_profile = {
    "name": "Alex",
    "theme": "space exploration",
    "difficulty": "medium",
    "interests": "rockets, aliens, sci-fi movies"
}

# Sample lesson content about Python variables
lesson_text = """
Python Variables - Introduction

A variable is a named container that stores a value in a program.
You create a variable by assigning a value to a name using the = operator.

Examples:
    name = "Alex"
    age = 15
    score = 100.5

Variable naming rules:
- Must start with a letter or underscore
- Cannot start with a number
- Cannot contain spaces (use underscores instead)
- Case sensitive (score and Score are different variables)

You can change the value of a variable at any time:
    score = 100
    score = 200  # score is now 200

Variables can store different types of data:
- Strings: text in quotes → name = "Alex"
- Integers: whole numbers → age = 15
- Floats: decimal numbers → score = 100.5
- Booleans: True or False → is_playing = True
"""

print("Generating your quest...")
print("-" * 40)

quest = generate_quest(student_profile, lesson_text)

if validate_quest(quest):
    print("✅ Quest generated successfully!\n")
    print(f"QUEST TITLE: {quest['quest_title']}")
    print(f"THEME: {quest['theme']}")
    print(f"\nSTORY: {quest['story_intro']}")
    print(f"\nLEARNING OBJECTIVE: {quest['learning_objective']}")
    print(f"\nNPC: {quest['npc_name']}")
    print(f"NPC SAYS: {quest['npc_dialogue']}")
    print(f"\nCHALLENGES:")
    for i, challenge in enumerate(quest['challenges'], 1):
        print(f"\n  Question {i}: {challenge['question']}")
        for option in challenge['options']:
            print(f"    - {option}")
        print(f"  Correct: {challenge['correct_answer']}")
    print(f"\nREWARD: {quest['reward']['badge_name']} (+{quest['reward']['xp']} XP)")
    print(f"MESSAGE: {quest['reward']['completion_message']}")
else:
    print("❌ Quest validation failed")