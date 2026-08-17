from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel, Field
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

Review = {
    "title": "Review",
    "description": "Structured representation of a phone review",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "A short summary of the phone review"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Positive aspects of the phone mentioned in the review"
        },
        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Negative aspects of the phone mentioned in the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["Positive", "Negative", "Neutral"],
            "description": "Overall sentiment of the review"
        },
        "reviewer": {
            "type": ["string", "null"],
            "description": "Name of the person who wrote the review, if mentioned"
        }
    },
    "required": [
        "summary",
        "pros",
        "cons",
        "sentiment",
        "reviewer"
    ]
}




structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""I’ve been using this phone for a few weeks and overall I’m quite happy with it. The display is bright and smooth, performance is fast for everyday tasks, and the camera takes good photos in daylight. Battery life is also decent and easily lasts most of the day with normal use. The design feels premium and comfortable to hold. However, the phone does get a little warm during heavy gaming, and the low-light camera could be better. Charging speed is also just average. Overall, it’s a reliable phone with good performance, display, and battery life, and I would recommend it for regular users. review by ayush tayal""")
print(result)
