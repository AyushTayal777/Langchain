from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.8)
result=model.invoke('tell me about india in 10 words')
print(result.text)