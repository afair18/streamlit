from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/submit-user")
async def submit_user(user: User):
    return {"message": f"이름: {user.name}, 나이: {user.age}"}
