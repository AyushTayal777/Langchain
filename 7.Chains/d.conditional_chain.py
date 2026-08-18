from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser= StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description='give the sentiment of the feedback')

parser2= PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative. \n {feedback} \n {format_instruction}',
    input_variables={'feedback'},
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifer_chain = prompt1 | model | parser2

prompt2= PromptTemplate(
    template='write an appropriate response to this positive feedback response \n {feedback}',
    input_variables={'feedback'}
)

prompt3= PromptTemplate(
    template='write an appropriate response to this negative feedback response \n {feedback}',
    input_variables={'feedback'}
)

parallel_chain = RunnableParallel({
    "feedback": lambda x: x["feedback"],
    "sentiment": classifier_chain
}) 

branch_chain= RunnableBranch(
    (lambda x:x["sentiment"].sentiment=='positive', prompt2 | model | parser),
    (lambda x:x["sentiment"].sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x:"could not find sentiment")
)

chain = parallel_chain | branch_chain

result = chain.invoke({'feedback':'This is a terrible phone'})

print(result)
chain.get_graph().print_ascii()