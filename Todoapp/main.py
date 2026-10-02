from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()
@app.get("/users/{user_id}")
async def userid(user_id):
    return {"user_id" : user_id}

@app.get("/users")
async def get_user(name):
    return {"Name" : name}

@app.post("/create-users")
async def create_user(name:str, age:int):
    return {
        "name" : name,
        "age" : age
    }