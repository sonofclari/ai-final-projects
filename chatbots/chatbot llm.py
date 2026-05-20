from openai import OpenAI

# Replace with your actual OpenRouter API key
OPENROUTER_API_KEY = "sk-or-v1-YOUR_KEY_HERE"

MODEL = "deepseek/deepseek-v4-flash:free"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Give short and concise answers in 2-3 lines."
    }
]

print("Chatbot started. Type 'exit' to quit.\n")

while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    # Keep last 10 messages + system prompt
    trimmed = [messages[0]] + messages[-10:]

    response = client.chat.completions.create(
        model=MODEL,
        messages=trimmed,
        max_tokens=200,
        temperature=0.5,
    )

    reply = response.choices[0].message.content
    print(f"Bot: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
