from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
loader = TextLoader("10.Text_splitters/text.txt")
docs=loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=5,
    
)

chunks= splitter.split_documents(docs)
print(len(chunks))
print(chunks[1].page_content)