from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password, verify_password


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        owner_id=user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


def get_task_by_id(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user_id
    ).first()


def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate, user_id: int):
    task = get_task_by_id(db, task_id, user_id)
    if not task:
        return None

    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int, user_id: int):
    task = get_task_by_id(db, task_id, user_id)
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task