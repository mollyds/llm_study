import gradio as gr
from chatbot_engine import chat
from dotenv import load_dotenv


def respond(message, chat_history):
    bot_message = chat(message)
    chat_history.append((message, bot_message))
    return "", chat_history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    load_dotenv()
    demo.launch()
