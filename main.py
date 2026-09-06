from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

model = pickle.load(open("model.pkl", "rb"))  

class CarInput(BaseModel):
    name: str
    company: str
    year: int
    kms_driven: int
    fuel_type: str

@app.get('/')
def home():
    return {'message': 'car price prediction'}

@app.post('/predict')
def predict_price(data: CarInput):
    input_df = pd.DataFrame([data.model_dump()])
    prediction_log = model.predict(input_df)
    predicted_price = np.exp(prediction_log[0])
    return {'predicted_price': round(float(predicted_price))}