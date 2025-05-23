# app/main.py
from fastapi import FastAPI
from .auth import router as auth_router
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Xyronix Auth Server")

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Xyronix Auth Server is up and running!"}