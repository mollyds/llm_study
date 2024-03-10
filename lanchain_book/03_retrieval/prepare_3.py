'''p107_分割した文章をベクトル化し、データベースに保存する'''
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=300,
    pipeline="ja_core_news_sm"
)
splitted_documents = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data", # 永続化データの保存先を指定
    embedding_function=embeddings # ベクトル化するためのモデルを指定
)

database.add_documents( #ドキュメントをデータベースに追加
    splitted_documents, # 追加するドキュメント
)

print("データベースの作成が完了しました")
