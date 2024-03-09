import json
import openai  #←OpenAIが用意しているPythonパッケージをインポートする

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="吾輩は猫である、名前は",
    stop="。",
    max_tokens=100,
    n=2,
    temperature=0.5
)

print(json.dumps(response, indent=2, ensure_ascii=False))
