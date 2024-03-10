'''p112_検索結果と質問を組み合わせて質問に答えさせる'''

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./data",
    embedding_function=embeddings
)

query = "飛行車の最高速度は?"

documents = database.similarity_search(query)
documents_string = "" # ドキュメントの内容を格納する変数を初期化
for document in documents:
    documents_string += f"""
-------------------------
{document.page_content}
""" # ドキュメントの内容を追加（Start）

prompt = PromptTemplate(
    template="""文章を元に質問に答えてください。
    
文章:
{document}

質問: {query}
""", # ドキュメントの内容を追加（End）

    input_variables=["document", "query"]
)

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

result = chat([
    HumanMessage(content=prompt.format(document=documents_string, query=query))
])

print(result.content)
