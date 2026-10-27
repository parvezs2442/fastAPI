from fastapi import FastAPI, HTTPException
import json


app = FastAPI() #object for fastAPI

@app.get("/") # EndPoint for homapage
def greet():
    return {"Hello and Welcome to FAST API"}

@app.get("/about")
def about():
    return {"Hello from about page"}

def load_data(): #function to load data from another file
    with open ("students.json", "r") as file:  #getting the data from file
        return json.load(file)  #loads the data from json file

@app.get("/student")
def students_data():
    return load_data()

#path parameter & error handling

@app.get("/students/{student_id}") #student id is our path parameter
def getStudent_by_ID(student_id:str):
    data = load_data()
    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student with Id-> {student_id} not found"
        )
    return data[student_id]
