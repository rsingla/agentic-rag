import os
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

api_key = os.environ["MISTRAL_API_KEY"]
mistral_model = "codestral-latest"
llm = ChatMistralAI(model=mistral_model, temperature=0, api_key=api_key)
result = llm.invoke([("user", "give me the code for finding a single fibonacci number given an input of x number ")])

parser = StrOutputParser()

parser.invoke(result)

print(result.content)