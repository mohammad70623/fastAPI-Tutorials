from fastapi import FastAPI 

app = FastAPI() 

@app.get("/")
def hello():
    return {'message': 'Patient Management system API'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to to manage your patient record'}
