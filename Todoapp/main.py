from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()
@app.get("/users/{user_id}")
async def userid(user_id):
    return {"user_id" : user_id}