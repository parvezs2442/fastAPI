from fastapi import FastAPI
import json


app = FastAPI() #object for fastAPI

@app.get("/") # EndPoint for homapage
def greet():
    return {"Hello and Welcome to FAST API"}

@app.get("/about")
def about():
    return {"Hello from about page"}

def get_data(): #function to get data
    with open ("students.json", "r") as file:  #getting the data from file
        return json.load(file)  #loads the data from json file

@app.get("/student")
def students_data():
    return get_data()