from fastapi import FastAPI
from app.generate_fake_data import generateFakeData

app = FastAPI()


@app.get("/")
def root(dataCount: int = 1000, deviceCount: int = 10):
    return { 'payload': generateFakeData(dataCount, deviceCount) }