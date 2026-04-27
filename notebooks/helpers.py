# Api Client
from anthropic import Anthropic
client = Anthropic()
model = "claude-sonnet-4-5-20250929"

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages):
    system = """
    You are a patient math tutor.
    Do not directly answer a student's questions.
    Guide them to a solution step by step.
    """
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        system=system
    )
    return message.content[0].text