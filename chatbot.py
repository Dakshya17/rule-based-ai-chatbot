#!/usr/bin/env python3
"""
chatbot.py
----------
A simple rule-based AI chatbot.

Architecture (IPO model):
    INPUT   -> Sanitize & normalize raw user text (lowercase, strip whitespace)
    PROCESS -> Match sanitized text against a dictionary-based knowledge base
    OUTPUT  -> Return a matching response, or a fallback if no rule matches

Run it with:
    python chatbot.py
"""

from knowledge_base import get_response, EXIT_COMMANDS

BOT_NAME = "RuleBot"


def sanitize(raw_input: str) -> str:
    """Normalize raw input: lowercase + strip leading/trailing whitespace."""
    return raw_input.lower().strip()


def print_banner() -> None:
    print("=" * 50)
    print(f"  {BOT_NAME} — Rule-Based AI Chatbot")
    print("  Type 'exit', 'quit', or 'bye' to end the chat.")
    print("=" * 50)


def chat() -> None:
    """Main conversation loop. Runs until an exit command is received."""
    print_banner()
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}. Ask me something, or say 'help'.")

    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        if not clean_input:
            print(f"{BOT_NAME}: Say something! I'm listening.")
            continue

        if clean_input in EXIT_COMMANDS:
            print(f"{BOT_NAME}: Goodbye! 👋")
            break

        reply = get_response(clean_input)
        print(f"{BOT_NAME}: {reply}")


if __name__ == "__main__":
    try:
        chat()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{BOT_NAME}: Session ended. Goodbye! 👋")
