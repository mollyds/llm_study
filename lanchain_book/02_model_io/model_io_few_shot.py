from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
"input": "LangChainはChatGPT・Large Language Model (LLM)の実利用をより実戦に簡易に行うためのツール群です",
"output": "LangChainは、ChatGPT・Large Language Model (LLM)の実利用をより実戦に、簡易に行うためのツール群です。"
    }
]

prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="入力: {input}\n出力: {output}",
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples, # プロンプトに挿入する例をリスト形式で設定する
    example_prompt=prompt, # 例を挿入する書式として、PromptTemplateを設定する
    prefix="以下の句読点の抜けた入力に句読点を追加してください。追加して良い引端点は「、」「。」のみです。他の句読点は追加しないでください。",
    suffix="入力: {input_string}\n出力:", # 例の後に挿入されるテキスト。今回のコードでは、ユーザからの入力=input_string。
    input_variables=["input_string"], # 全体のプロンプトが期待する変数名のリスト（←？よく分からん2024/3/8）
)

llm = OpenAI()
formatted_prompt = few_shot_prompt.format(
    input_string="私はさまざまな機能がジュールとして提供されているLangChainを使ってアプリケーションを開発しています"
)
result = llm.predict(formatted_prompt)
print("formatted prompt: ", formatted_prompt)
print("result: ", result)

