# 結果を日時形式で受け取る
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.schema import HumanMessage

output_parser = DatetimeOutputParser()

chat = ChatOpenAI(model="gpt-3.5-turbo", )

prompt = PromptTemplate.from_template("{product}のリリース日を教えて")

result = chat(
   [
       HumanMessage(content=prompt.format(product="iPhone10")),
       HumanMessage(content=output_parser.get_format_instructions()),
   ]
)

output = output_parser.parse(result.content)

print(output)