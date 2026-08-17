from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Review(TypedDict):
    key_themes:Annotated[list[str],"write down all the key themes discussed in the review"]
    summary:Annotated[str,"a brief summary of the review"]
    sentiment:Annotated[Literal["pos","neg"],"return sentiment of the review wither positive or negative"]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""I’ve been using this phone for a few weeks and overall I’m quite happy with it. The display is bright and smooth, performance is fast for everyday tasks, and the camera takes good photos in daylight. Battery life is also decent and easily lasts most of the day with normal use. The design feels premium and comfortable to hold. However, the phone does get a little warm during heavy gaming, and the low-light camera could be better. Charging speed is also just average. Overall, it’s a reliable phone with good performance, display, and battery life, and I would recommend it for regular users.""")
print(result)
print(result['summary'])
print(result['sentiment'])