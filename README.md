🚀 Task Manager Backend API (FastAPI)

A secure and scalable Task Management Backend API built using FastAPI, featuring JWT authentication, user management, and full CRUD operations for tasks. This project demonstrates backend architecture, authentication, and RESTful API development.

# Task Manager Backend API (FastAPI)

Live API: https://task-manager-backend-fastapi-od1g1eke1-ruchi1.vercel.app  
API Docs: https://task-manager-backend-fastapi-od1g1eke1-ruchi1.vercel.app/docs

A secure and scalable Task Management Backend API built using FastAPI.


✨ Features
User Registration and Login
JWT Authentication
Create Tasks
Get User Tasks
Update Tasks
Delete Tasks
Protected Routes
SQLite Database Integration
RESTful API Design
Interactive Swagger Documentation
Tech Stack
Python
FastAPI
SQLAlchemy
SQLite
JWT (python-jose)
Pydantic
Uvicorn

📡 API Endpoints
Authentication

POST /register — Register a new user
POST /login — Login and receive access token

🛠️ Tech Stack
POST /tasks — Create a task
GET /tasks — Get all tasks
PUT /tasks/{task_id} — Update a task
DELETE /tasks/{task_id} — Delete a task

▶️ Run Locally
Clone the repository

git clone https://github.com/Dhakadruchi6/task-manager-backend-fastapi.git
cd task-manager-backend-fastapi

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn app.main:app --reload

Open in browser

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
RESTful API implementation
Database integration using SQLAlchemy
Protected endpoints
Production-ready project structure
Swagger API documentation

👩‍💻 Author
Ruchi Dhakad
Full Stack Developer | Backend Enthusiast
GitHub: https://github.com/Dhakadruchi6
