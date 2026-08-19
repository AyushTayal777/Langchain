from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="9.Document_loaders/test",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
print(len(docs))