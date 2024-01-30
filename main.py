from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    ticker: str
    price: float

@app.post("/submit-user")
def submit_user(user: User):
    print(f"Received user data: 종목 - {user.ticker}, 가격 - {user.price}")
    return {"message": f"종목: {user.ticker}, 가격: {user.price}"}
