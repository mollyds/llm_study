'''p160_ConversationChainを使って処理を簡潔にする'''

import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  #← ConversationBufferMemoryをインポート
# from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

memory = ConversationBufferMemory( #← メモリを初期化
    return_messages=True
)

chain = ConversationChain(
    memory=memory,
    llm=chat
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="私は会話の文脈を考慮した返答ができるチャットボットです。メッセージを入力してください。").send()

@cl.on_message
async def on_message(message: str):
    result = chain(
        message
    )
    # 以下全部不要に。
    # memory_message_result = memory.load_memory_variables({}) #← メモリの内容を取得
    # messages = memory_message_result['history'] #← メモリの内容からメッセージのみを取得
    # messages.append(HumanMessage(content=message)) #← ユーザーからのメッセージを追加
    # memory.save_context(  #← メモリにメッセージを追加
    #     {
    #         "input": message,  #← ユーザーからのメッセージをinputとして保存
    #     },
    #     {
    #         "output": result.content,  #← AIからのメッセージをoutputとして保存
    #     }
    # )
    await cl.Message(content=result["response"]).send() #← AIからのメッセージを送信
