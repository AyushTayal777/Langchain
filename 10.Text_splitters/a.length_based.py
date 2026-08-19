from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
loader = TextLoader("10.Text_splitters/text.txt")
docs=loader.load()
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=5,
    separator=''
)

result= splitter.split_documents(docs)
print(result[0])