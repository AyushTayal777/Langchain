from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')
prompt= PromptTemplate(
    template='write a 3 line summary of the following {poem}',
    input_variables={'poem'}
)

parser= StrOutputParser()

chain = prompt | model | parser
loader=TextLoader("9.Document_loaders/cricket.txt", encoding='utf-8')

docs= loader.load()
result = chain.invoke({"poem":docs[0].page_content})


print(result)