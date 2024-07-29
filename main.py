from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

app = FastAPI()

class InputText(BaseModel):
    input: str

template = """
You are a helpful assistant
"""

model = ChatOllama(
    model="tinydolphin",
    temperature=0,
)

system_prompt = SystemMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([system_prompt, ("human", "{input}")])

@app.post("/invoke")
def invoke_chain(input_text: InputText):
    chain = chat_prompt | model
    result = chain.invoke({"input": input_text.input})
    return {"response": result.content}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Narvaez API"}
