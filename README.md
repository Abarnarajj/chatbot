# 🤖 LLaMA 3.2 Bot – AI Chatbot 🚀  

LLaMA 3.2 Bot is an **AI-powered chatbot** built using **FastAPI** for the backend, **HTML, CSS, JavaScript** for the frontend, and **SQLite3** for storing chat history. It integrates **LLaMA 3.2** via **Ollama** to generate intelligent responses in real-time.  

## 🌟 Features  
- ⚡ **FastAPI Backend** – High-performance, async API.  
- 🤖 **LLaMA 3.2 Integration** – Uses Ollama to run the model.  
- 🗄 **SQLite3 Database** – Stores chat history for future reference.  
- 📡 **Real-time Communication** – Fetches AI responses dynamically.  
- 🔌 **Easy Deployment** – Lightweight & scalable solution.  

### 🏗 Tech Stack
**Backend:** FastAPI
**Frontend:** HTML, CSS, JavaScript
**Database:** SQLite3
**AI Model:** LLaMA 3.2 (via Ollama)


## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Abarnarajj/chatbot.git
cd chatbot
```
### 2️⃣ Install Ollama (Required for LLaMA 3.2)
```bash
curl -fsSL https://ollama.com/install.sh | sh   # macOS/Linux
winget install Ollama.Ollama                    # Windows
ollama run llama3.2
```
### 3️⃣ Create a Virtual Environment & Activate It
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
### 4️⃣ Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy sqlite3 pydantic ollama
```
### 5️⃣ Run the Backend Server
```bash
uvicorn main:app --reload
```
### 6️⃣ Open the Chatbot
Open index.html in a browser.

### 🛠 Database Setup (SQLite3)
The chatbot stores chat history using SQLite3. The database.py file handles database connections.
## To Create a Database
```bash
python create_db.py
```


