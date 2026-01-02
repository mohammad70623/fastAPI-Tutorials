from fastapi import FastAPI
from pydantic import BaseModel, computed_field, Field 
from typing import Literal 
import pickle 
import pandas as pd

#import the ML model 
with open('fraud detection pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

