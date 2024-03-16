'''p184_LLMChainを使って複数のモジュールをまとめる'''
from tabnanny import verbose
from langchain import LLMChain, PromptTemplate  #← LLMChainをインポート
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(  
    model="gpt-3.5-turbo",  
)

prompt = PromptTemplate(  
    template="{product}はどこの会社が開発した製品ですか？",  
    input_variables=[
        "product"  
    ]
)

chain = LLMChain( #← LLMChainを作成する
    llm=chat,
    prompt=prompt,
    verbose=True
)

result = chain.predict(product="iPhone") #← LLMChainを実行する

print(result)