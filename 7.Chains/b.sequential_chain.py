from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.6-flash")

template1= PromptTemplate(
    template='write a detailed summary on {topic}',
    input_variables={'topic'}
)

template2 = PromptTemplate(
    template='identfy main theme of the following text. /n {text}',
    input_variables={'text'}
)

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic': 'Avengers Doomsday'})
print(result)
chain.get_graph().print_ascii()