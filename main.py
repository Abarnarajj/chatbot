from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Conversation
import ollama
from pydantic import BaseModel

# Initialize FastAPI App
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Model for API Request
class MessageRequest(BaseModel):
    user_message: str

# 1️⃣ Send message to chatbot
@app.post("/chat/")
def chat_with_bot(request: MessageRequest, db: Session = Depends(get_db)):
    user_message = request.user_message

    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": user_message}])
    bot_response = response["message"]["content"]

    # Store conversation in DB
    new_chat = Conversation(user_message=user_message, bot_response=bot_response)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return {"user_message": user_message, "bot_response": bot_response}

# 2️⃣ Get all conversations
@app.get("/conversations/")
def get_conversations(db: Session = Depends(get_db)):
    chats = db.query(Conversation).all()
    return chats

# 3️⃣ Delete all conversations
@app.delete("/conversations/")
def delete_conversations(db: Session = Depends(get_db)):
    db.query(Conversation).delete()
    db.commit()
    return {"message": "All conversations deleted"}
