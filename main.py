from fastapi import FastAPI

app = FastAPI()   #object of fastAPI

@app.get("/") #route for homepage
def greet():
    return {"Hello and Welcome to FAST API"}