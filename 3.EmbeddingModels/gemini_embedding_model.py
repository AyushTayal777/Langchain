from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=GoogleGenerativeAIEmbeddings(model='gemini-embedding-2',dimensions=4)
result=embedding.embed_query("Delhi is capital of india")
print(str(result))