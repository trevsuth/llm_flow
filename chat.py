from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

model = ChatOllama(
    model="tinydolphin",
    temperature=0,
)

messages = [
    ('system','You are a helpful assistant'),
    ('human', 'Tell me a joke')
]

chat = model.invoke(messages)
print(chat.content)