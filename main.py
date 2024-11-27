from ChatBot import ChatBot
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Body
from pydantic import BaseModel

class Item(BaseModel):
    question: str

app = FastAPI()
chatBot = ChatBot()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    question: str

@app.post("/question")
def post_question(item: Item): 
    response = chatBot.get_response(item.question)

    print(response)

    return { "response": response }