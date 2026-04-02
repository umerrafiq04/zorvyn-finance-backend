from fastapi import FastAPI
from database import engine, Base
import models
from routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

# include routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Finance Backend is running "}