from fastapi import FastAPI
from app.manager import DataManager

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Malicious Text Feature Engineering System is running!"}

@app.get("/processed-data")
def get_processed_data():
    manager = DataManager()
    data = manager.get_processed_data()
    return data[:5]  