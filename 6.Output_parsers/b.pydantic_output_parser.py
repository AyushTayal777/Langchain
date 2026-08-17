from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int=Field(description='age of the person')
    city:str=Field(description='name of the city the person belongs to')

parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template='Generate the name, city and age of a fictional {place} person \n {format_instruction}', 
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain= template | model | parser
final_result= chain.invoke({'place':'indian'})
print(final_result)