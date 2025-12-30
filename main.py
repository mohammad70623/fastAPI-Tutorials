from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message': 'Patient Management system API'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to to manage your patient record'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description='ID of the patient in the DB', example='P001')):
    #load all the patient 
    data = load_data() 

    if patient_id in data:
        return data[patient_id]
    return {'Error':'patient does not found'}

