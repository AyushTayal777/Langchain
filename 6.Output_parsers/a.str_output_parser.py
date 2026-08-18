from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables={'topic'}
)
template2=PromptTemplate(
    template='write a 3 line summary on the following text. /n {text}',
    input_variables={'text'}
)

parser=StrOutputParser()

chain= template1 | model | parser | template2 | model | parser
result= chain.invoke({'topic':'black hole'})
print(result)