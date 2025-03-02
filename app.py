import chainlit as cl
import requests

# FastAPI Server URL
API_URL = "http://127.0.0.1:8000/chat/"

@cl.on_message
async def on_message(message: cl.Message):
    response = requests.post(API_URL, json={"user_message": message.content}).json()
    
    await cl.Message(content=response["bot_response"]).send()
