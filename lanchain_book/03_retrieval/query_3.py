'''p130_RearievalQAを使ってコードを簡単に'''
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

chat = ChatOpenAI(model="gpt-3.5-turbo")

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings
)

retriever = database.as_retriever() # データベースをRetrieverに変換する

qa = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True # 返答にソースドキュメントを含めるかどうか
)

result = qa("飛行車の最高速度を教えて")

print(result["result"])
print(result["source_documents"])
