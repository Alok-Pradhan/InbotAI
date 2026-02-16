import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class LLMService:
    def __init__(self):
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")

        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

    def generate(self, context: str, question: str, history=None):

        messages = [
            {
                "role": "system",
                "content": "You are a formal hospital AI assistant. Use provided context only."
            }
        ]

        # Add conversation history
        if history:
            messages.extend(history)

        # Add current question
        messages.append({
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{question}"
        })

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.3
        )

        return response.choices[0].message.content

