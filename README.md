# 🔮 Chronicler's Academy

> *Where knowledge becomes legend.*

An AI-powered RPG learning app that transforms your notes and PDFs into personalized quests, challenges, and XP progression. Built with Streamlit and powered by Groq's LLaMA models.

---

## ✨ Features

- **📜 Quest Generation** — Upload a PDF or paste your notes and the AI generates a fully personalized RPG quest based on your content
- **🧙 The Chronicler** — An ancient, sardonic AI mentor who answers questions about your material before you embark on your quest
- **⚔️ Challenge System** — Multiple-choice trials pulled directly from your lesson content, difficulty-scaled to your level
- **⚡ XP & Rank Progression** — Earn XP for completing quests, correct answers, no-hint runs, and perfect scores. Rank up from Apprentice to Chrono-Legend
- **🔥 Daily Streak System** — Login streaks with grace periods, milestone badges (Ember Keeper → Week Warden → Fortnight Forged → Eternal Chronicler), and XP bonuses
- **📚 Academy Archive** — Full history of every dimension (quest) you've completed
- **🎯 Personalization Quiz** — Scholar profile built from your theme, interests, play style, and hero type — the Chronicler and quests adapt to you
- **🌑 Dark RPG Theme** — Void black, arcane violet, and rune gold visual identity

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit 1.58 |
| AI / LLM | Groq API — LLaMA 3.3 70B Versatile |
| Vision | Groq LLaMA 3.2 11B Vision (PDF extraction) |
| Database | SQLite via Python `sqlite3` |
| PDF parsing | PyMuPDF (`fitz`) |
| Language | Python 3.11+ |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- A [Groq API key](https://console.groq.com) (free tier available)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOURUSERNAME/chroniclers-academy.git
cd chroniclers-academy

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your environment variables
cp .env.example .env
# Then edit .env and add your GROQ_API_KEY
```

### Running the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
chroniclers-academy/
├── app.py                          # Main Streamlit app — all pages & routing
├── backend/
│   ├── database.py                 # SQLite schema, queries, XP/rank logic
│   ├── quest_generator.py          # Groq quest generation + fallback
│   ├── difficulty_prompts.py       # Difficulty-aware prompt builder
│   ├── chronicler_prompts.py       # Chronicler personality & chat prompts
│   ├── streak_manager.py           # Streak logic (increment/freeze/reset)
│   ├── streak_migration.py         # DB migration + streak persistence
│   ├── vision_extractor.py         # PDF vision extraction via Groq
│   └── fallback_quest.py           # Hardcoded fallback quest
├── ui/
│   ├── theme.py                    # Dark RPG CSS theme + component builders
│   └── streak_ui.py                # Streak panel, badge, milestone road
├── data/
│   └── scholars.db                 # SQLite database (git-ignored)
├── .streamlit/
│   └── config.toml                 # Streamlit dark theme config
├── .env                            # API keys (git-ignored)
├── .env.example                    # Template for environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🎮 Demo Flow

1. **Create a Scholar** — choose your name, PIN, theme, difficulty, and interests
2. **Complete the Quiz** — optional personalization for deeper customization
3. **Upload content** — PDF or pasted text (lecture notes, textbook chapters, anything)
4. **Consult The Chronicler** — ask questions about your material before the quest
5. **Generate a Quest** — AI builds a personalized RPG quest from your content
6. **Complete Challenges** — answer questions, use hints, earn XP
7. **Rank Up** — watch your XP bar fill and your rank climb
8. **Check the Archive** — review every dimension you've conquered

---

## 🏆 Rank System

| Rank | Title | XP Required |
|---|---|---|
| I | Apprentice Chrono-Scholar | 0 |
| II | Adept Chrono-Scholar | 200 |
| III | Dimensional Seeker | 500 |
| IV | Master of Realms | 1,000 |
| V | Chrono-Legend | 2,000 |

---

## ⚡ XP System

| Action | XP |
|---|---|
| Quest completion | +50 |
| Correct answer | +30 |
| No hints used bonus | +20 |
| Perfect score bonus | +50 |
| Streak milestone (3d/7d/14d/30d) | +30 / +75 / +150 / +400 |

---

## 🔥 Streak Milestones

| Streak | Badge | Bonus XP |
|---|---|---|
| 3 days | 🔥 Ember Keeper | +30 |
| 7 days | 🔥🔥 Week Warden | +75 |
| 14 days | 💎🔥 Fortnight Forged | +150 |
| 30 days | 👑🔥 Eternal Chronicler | +400 |

> **Grace period:** miss 1 day and your streak freezes instead of resetting. Miss 2+ days and it resets to 1.

---

## 🗺️ Roadmap

### In Progress
- [ ] Visual polish pass — CSS class system, sidebar nav, mockup parity

### Planned (v2)
- [ ] Class system with perks
- [ ] Pet companion system
- [ ] Life bar mechanic
- [ ] Battle minigame
- [ ] Armor system
- [ ] Character sprites (Ren'Py or React)
- [ ] Multiplayer leaderboard

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📦 Requirements

Generate with:
```bash
pip freeze > requirements.txt
```

Key dependencies:
- `streamlit`
- `groq`
- `python-dotenv`
- `PyMuPDF`

---

## 📄 License

MIT License — feel free to fork, extend, and build your own Academy.

---

*Built with 🔮 and a lot of Groq API calls.*
