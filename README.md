# 🤖 RuleBot — Rule-Based AI Chatbot

A simple, dependency-free rule-based chatbot built in Python. This is **Project 1**
of the DecodeLabs AI Industrial Training Kit — the foundation phase focused on
control flow and logic before moving into machine learning-based systems.

## ✨ Features

- **Continuous conversation loop** — chat runs until you say `exit`, `quit`, or `bye`
- **Input sanitization** — handles mixed case and stray whitespace (`"HeLLo  "` → `"hello"`)
- **Dictionary-based knowledge base** — O(1) intent lookup instead of a long if/elif ladder
- **Keyword/substring matching** — recognizes intents even inside full sentences
  (e.g. `"hi there!"` still triggers the greeting intent)
- **7 built-in intents**: greeting, farewell, thanks, how are you, identity, help, jokes
- **Randomized responses** — avoids sounding robotic/repetitive
- **Graceful fallback** — a friendly default reply for anything it doesn't recognize
- **Unit tested** with Python's built-in `unittest`

## 🗂 Project Structure

```
rule-based-ai-chatbot/
├── chatbot.py          # Main entry point — input loop, sanitization, output
├── knowledge_base.py   # Intents, keywords, responses, and matching logic
├── tests/
│   └── test_chatbot.py # Unit tests for the knowledge base
├── requirements.txt    # (No external dependencies — standard library only)
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+

### Run it

```bash
git clone https://github.com/<your-username>/rule-based-ai-chatbot.git
cd rule-based-ai-chatbot
python chatbot.py
```

### Example session

```
==================================================
  RuleBot — Rule-Based AI Chatbot
  Type 'exit', 'quit', or 'bye' to end the chat.
==================================================
RuleBot: Hi! I'm RuleBot. Ask me something, or say 'help'.
You: hello
RuleBot: Hey there! How can I help you today?
You: how are you
RuleBot: I'm just a set of rules, but I'm running smoothly! How about you?
You: tell me a joke
RuleBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
RuleBot: Goodbye! 👋
```

### Run the tests

```bash
python -m unittest discover
```

## 🧠 How It Works (Architecture)

This follows a simple **Input → Process → Output (IPO)** model:

1. **Input**: Raw text is captured from the user each loop iteration.
2. **Sanitize**: The text is lowercased and stripped of whitespace so
   `"Hello"`, `"hello"`, and `"  hello  "` are all treated identically.
3. **Process**: The cleaned input is checked against a dictionary of intents.
   Each intent has a list of trigger keywords — if any keyword appears as a
   substring of the input, that intent's response pool is used.
4. **Output**: A response is chosen (randomly, from the matched intent's
   list) and printed. If nothing matches, a fallback response is returned.

### Why a dictionary instead of if/elif?

| Approach          | Lookup Time | Maintainability   |
|--------------------|:-----------:|:-----------------:|
| if/elif ladder     | O(n)        | Gets messy fast    |
| Dictionary + `.get()` | O(1) avg | Clean, extensible  |

Using a dictionary keeps all rules as data (not nested code), so adding a
new intent is as simple as adding one entry to `INTENTS` in
`knowledge_base.py` — no new branches required.

## 🔧 Extending the Bot

Want to add a new intent? Open `knowledge_base.py` and add an entry:

```python
INTENTS["weather"] = {
    "keywords": ["weather", "forecast", "rain"],
    "responses": [
        "I can't check live weather yet, but I hope it's sunny where you are!",
    ],
}
```

Other ideas to extend this project:
- Add a **conversation memory** so the bot remembers the user's name
- Add **nested conditions** for multi-turn intents (e.g. asking a follow-up question)
- Swap the CLI for a simple **Flask/HTML web UI**
- Log conversations to a file for later review
- Use this as the deterministic "guardrail" layer in front of an LLM (see Project 2)

## 📌 Roadmap: From Rules to Vectors

This project uses **exact keyword matching** — a rigid, discrete mapping.
The next step in the DecodeLabs track (Project 2) moves toward **semantic
matching** using vector embeddings, so the bot can understand meaning and
paraphrasing rather than only exact keywords.

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 🙌 Credits

Built as part of the **DecodeLabs AI Industrial Training Kit — Batch 2026**.
