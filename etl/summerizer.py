from openai import OpenAI

client = OpenAI()

def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize AI news:\n{text}"}
        ]
    )
    return response.choices[0].message.content
