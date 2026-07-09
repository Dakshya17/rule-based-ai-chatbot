"""
knowledge_base.py
------------------
This module holds the chatbot's "brain": a dictionary-based knowledge base
that maps intents to keywords and responses.

Why a dictionary instead of if/elif/else?
    An if-elif ladder checks conditions one by one -> O(n) time and it gets
    unreadable fast as rules grow. A dictionary lookup is O(1) on average
    and keeps every rule in one clean, extensible data structure.
"""

import random
import re

# ---------------------------------------------------------------------------
# INTENTS
# Each intent has:
#   - keywords: words/phrases that trigger this intent (checked as substrings
#     of the sanitized user input, so "hello there" still matches "hello")
#   - responses: a list of possible replies (a random one is chosen, so the
#     bot doesn't sound robotic/repetitive)
# ---------------------------------------------------------------------------
INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening", "yo"],
        "responses": [
            "Hey there! How can I help you today?",
            "Hello! What's on your mind?",
            "Hi! Great to see you.",
        ],
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "farewell", "later"],
        "responses": [
            "Goodbye! Have a great day.",
            "See you soon!",
            "Take care!",
        ],
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "appreciate it", "thx"],
        "responses": [
            "You're welcome!",
            "Anytime!",
            "Glad I could help.",
        ],
    },
    "how_are_you": {
        "keywords": ["how are you", "how's it going", "how are u", "hows it going"],
        "responses": [
            "I'm just a set of rules, but I'm running smoothly! How about you?",
            "Doing great, thanks for asking!",
        ],
    },
    "identity": {
        "keywords": ["your name", "who are you", "what are you"],
        "responses": [
            "I'm RuleBot — a simple rule-based chatbot built with Python.",
            "You can call me RuleBot. I run on logic, not learning!",
        ],
    },
    "help": {
        "keywords": ["help", "what can you do", "commands", "options"],
        "responses": [
            "I can chat about greetings, how you're doing, and basic questions. "
            "Try saying 'hello', 'how are you', or 'bye'.",
        ],
    },
    "creator": {
        "keywords": ["who made you", "who created you", "your creator"],
        "responses": [
            "I was built as Project 1 of the DecodeLabs AI Industrial Training Kit.",
        ],
    },
    "joke": {
        "keywords": ["joke", "make me laugh", "funny"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I told my computer I needed a break, and it said 'No problem, "
            "I'll go to sleep.'",
        ],
    },
}

# Words that, if typed alone, immediately end the chat loop.
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "stop"}

# Fallback responses used when no intent matches (rotated randomly).
FALLBACK_RESPONSES = [
    "I don't quite understand that yet. Could you rephrase it?",
    "Hmm, I'm not sure how to respond to that. Try 'help' to see what I can do.",
    "I don't have a rule for that one. I'm still learning my responses!",
]


def get_response(user_input: str) -> str:
    """
    Match sanitized user input against the knowledge base and return a
    response. Falls back to a default message if nothing matches.

    This uses a two-step strategy:
      1. Fast exact-match style scan via keyword substring checks (rule-based).
      2. dict.get()-style fallback if nothing matches (single atomic default).
    """
    for intent, data in INTENTS.items():
        for keyword in data["keywords"]:
            # Word-boundary match: avoids false positives like the keyword
            # "yo" matching inside the word "you".
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, user_input):
                return random.choice(data["responses"])

    return random.choice(FALLBACK_RESPONSES)
