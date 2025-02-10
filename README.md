# YoyoStoryTime - Story Generation API  

## 🚀 Overview  
YoyoStoryTime is a Flask-based API that generates AI-powered bedtime stories using OpenAI's GPT model.  

## 📦 Features  
- Generate personalized story based on predefined characters and scenes.  
- Read the story using text-to-speed techniques
- Generate comic images 

## 🛠 Setup & Run  
### 1️⃣ Clone the Repository
```bash
git clone <repo-url>
cd YoyoStoryTime
```

### 2️⃣ Create the .env file
```
OPENAI_API_KEY=your_openai_api_key
```

### 3️⃣ Start the Docker & Run the Flask Application
```bash
docker compose up --build 
```

### 4️⃣ Test the API
```bash
curl -X POST http://127.0.0.1:8008/api/story/generate \
     -H "Content-Type: application/json" \
     -d '{"characters": ["Alice", "Bob"], "scene": "forest"}'
```

###

## ✅ To-Do List
### 🔹 Backend (API)  
- [x] **Story Generation API**: AI-generated stories with structured templates.  
- [ ] **Audio Generation API**: Convert generated stories into speech using TTS.  
- [ ] **Comic Generation API**: Generate visual comics based on the story.  

### 🔹 Frontend (Web & iOS)  
- [ ] **Web App**: Create a user-friendly UI for generating and listening to stories.  
- [ ] **iOS App (SwiftUI)**: Build an iOS app for interactive story playback.  

---
🚀 **This is our roadmap for YoyoStoryTime development!**  


## 📜 License
MIT License