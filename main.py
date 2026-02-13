import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Sentiment Analysis API using Groq")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set")

client = Groq(api_key=GROQ_API_KEY)


class Sentence(BaseModel):
    text: str


@app.get("/")
def health():
    return {"status": "API is running"}


@app.post("/predict")
def predict(sentence: Sentence):
    try:
        prompt = f"""
        Classify the sentiment of the following sentence as either
        POSITIVE or NEGATIVE. Only return one word.

        Sentence: "{sentence.text}"
        """

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        sentiment = completion.choices[0].message.content.strip()

        return {
            "input": sentence.text,
            "sentiment": sentiment
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
