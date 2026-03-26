🚀 Task Manager Backend API (FastAPI)

A secure and scalable Task Management Backend API built using FastAPI, featuring JWT authentication, user management, and full CRUD operations for tasks. This project demonstrates backend architecture, authentication, and RESTful API development.

✨ Features
🔐 User Registration & Login
🔑 JWT Authentication
📝 Create Tasks
📋 Get User Tasks
✏️ Update Tasks
❌ Delete Tasks
🛡️ Protected Routes
🗄️ SQLite Database Integration
⚡ FastAPI Swagger Documentation
🔄 RESTful API Design
🛠️ Tech Stack
Python
FastAPI
SQLAlchemy
SQLite
JWT Authentication
Pydantic
Uvicorn
📡 API Endpoints
Authentication
POST /register → Register new user
POST /login → Login and get access token
Tasks
POST /tasks → Create task
GET /tasks → Get all tasks
PUT /tasks/{task_id} → Update task
DELETE /tasks/{task_id} → Delete task
▶️ Run Locally
git clone https://github.com/Dhakadruchi6/task-manager-backend-fastapi.git
cd task-manager-backend-fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000/docs
📂 Project Structure
task-manager-backend-fastapi
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── crud.py
│
├── requirements.txt
└── README.md
🎯 Key Highlights
Clean backend architecture
JWT-based authentication
Database integration using SQLAlchemy
RESTful API design
Production-ready structure
Swagger API documentation
👩‍💻 Author

Ruchi Dhakad
Full Stack Developer | Backend Enthusiast
GitHub: https://github.com/Dhakadruchi6
