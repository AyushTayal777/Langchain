from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel, Field
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Review(BaseModel):
    key_themes:list[str]=Field(description="write down all the key themes discussed in the review")
    summary:str=Field(description="a brief summary of the review")
    sentiment:Literal["pos","neg"]=Field(description="return sentiment of the review wither positive or negative")
    pros:Optional[list[str]]=Field(default=None, description="Write down all the pros inside a list")
    cons:Optional[list[str]]=Field(default=None, description="Write down all the cons inside a list")
    name:Optional[str]=Field(default=None, description="write the name of the reviewer")
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""I’ve been using this phone for a few weeks and overall I’m quite happy with it. The display is bright and smooth, performance is fast for everyday tasks, and the camera takes good photos in daylight. Battery life is also decent and easily lasts most of the day with normal use. The design feels premium and comfortable to hold. However, the phone does get a little warm during heavy gaming, and the low-light camera could be better. Charging speed is also just average. Overall, it’s a reliable phone with good performance, display, and battery life, and I would recommend it for regular users. review by ayush tayal""")
print(result)
