from langchain_ollama import ChatOllama
from langchain_core.prompts import (SystemMessagePromptTemplate, ChatPromptTemplate)

template = """
You are a creative consultant brainstorming for a business.  

You must follow the following principles:
{principles}

Please generate a numerical list of five catchy names for a start-up in the {industry} industry that deals with {context}?

Here is an example of the format:
1. Name 1
2. Name 2
3. Name 3
4. Name 4
5. Name 5
"""

model = ChatOllama(
    model="tinydolphin",
    temperature=0,
)

system_prompt = SystemMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([system_prompt])

chain = chat_prompt | model

result = chain.invoke({
    "industry":"medical",
    "context" :  "creating AI solutions by summarizing patient histories",
    "principles": '''1. Each name should be short and easy to remember. 2. Each name should be easy to pronounce. 3. Each name should be unique and not already used by another company.'''
})

print(result.content)