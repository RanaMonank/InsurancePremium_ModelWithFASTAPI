from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION
from schema.prediction_response import PredictionResponse
import pandas as pd
import os

app = FastAPI()
            
@app.get('/')
def home():
    return {'message':'Insurance Prediction API'}

@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version':MODEL_VERSION,
        "model": model is not None
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    
    user_data = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    # model = app.state.model
    try:
        prediction = predict_output(user_data)
        
        return JSONResponse(status_code=200, content={'responce': prediction})
    
    except Exception as e:
        
        return JSONResponse(status_code=500, content=str(e))