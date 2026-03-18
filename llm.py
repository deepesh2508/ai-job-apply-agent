from openai import OpenAI
from config import OPENAI_API_KEY, USER_PROFILE

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(question):
    prompt = f"""
    You are filling a job application form.

    Candidate Profile:
    {USER_PROFILE}

    Question: {question}

    Instructions:
    - Answer in 2-3 lines
    - Pick only relevant info
    - Focus on impact (numbers, scale)
    - Be professional and concise

    Answer:
    """

    res = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content.strip()