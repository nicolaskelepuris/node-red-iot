from fastapi import Body, FastAPI
from app.generate_fake_data import generateFakeData
from app.notifier import notify

app = FastAPI()


@app.get("/generate-fake-data")
def root(dataCount: int = 1000, deviceCount: int = 10):
    return { 'payload': generateFakeData(dataCount, deviceCount) }

@app.post("/notify")
def root(payload: dict = Body(...)):
    return { 'payload': notify(payload) }