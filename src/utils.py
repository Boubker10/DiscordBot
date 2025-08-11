import requests


def get_prompt(message): 
    prompt = f"""You are discord bot, a friendly and intelligent assistant chatting on Discord.
Respond in a concise, clear, and context-aware manner.

Context:
- Message: "{message}"

Rules:
1. Use a tone suitable for a Discord chat (natural, clear).
2. Do not provide personal information.
3. If the question is ambiguous, ask for clarification.
4. If it’s a bot command (prefix '!'), execute or explain the command.
5. Stay in the role of a Discord assistant.

Answer:
"""
    return prompt.format(message=message)





def call_deepseek_api(user_input, api_key, base_url, model):
    prompt =get_prompt(user_input)
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(base_url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
