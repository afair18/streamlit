from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    ticker: str
    price: float

@app.post("/data")
def submit_user(user: Data):
    print(f"Received user data: 종목 - {user.ticker}, 가격 - {user.price}")
    return {"message": f"종목: {user.ticker}, 가격: {user.price}"}
