from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from .database import SessionLocal, engine, Base
from . import models, schemas, crud
from .auth import create_access_token, SECRET_KEY, ALGORITHM

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager Backend API")
security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = crud.get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user


@app.get("/")
def root():
    return {"message": "Task Manager Backend API is running"}


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_task(db, task, current_user.id)


@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.get_tasks(db, current_user.id)


@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    updated_task = crud.update_task(db, task_id, task, current_user.id)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    deleted_task = crud.delete_task(db, task_id, current_user.id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}