# p73-74結果を逐次表示させる
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    streaming=True,
    callbacks=[
        StreamingStdOutCallbackHandler()
    ]
)

resp = chat([
    HumanMessage(content="おいしいステーキの焼き方を教えて")
])


