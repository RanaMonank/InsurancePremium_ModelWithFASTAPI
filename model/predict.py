import joblib
import pandas as pd
import pickle

# filename = r'D:/FastAPI/Insurance_Premium_Model/model/model.joblib'
model = joblib.load("model/model.joblib")
# with open("model/model.joblib", 'rb') as f:
#     model = pickle.load(f)

MODEL_VERSION = '1.0.0'

class_label = model.classes_.tolist()
def predict_output(user_input: dict):
    
    input_data = pd.DataFrame([user_input])
    
    output = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities)
    
    class_probs = dict(zip(class_label, map(lambda p: round(p, 4), probabilities)))
    
    return {
        "prediction_category":output,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }