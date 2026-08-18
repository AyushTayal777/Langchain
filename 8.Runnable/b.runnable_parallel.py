from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser= StrOutputParser()

prompt1=PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables={'topic'}
)

prompt2=PromptTemplate(
    template='generate a linkedin post about {topic}',
    input_variables={'topic'}
)

parallel_chain= RunnableParallel({
    "tweet" : RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2,model,parser)

})

result= parallel_chain.invoke({'topic':'AI'})

print(result)