import pickle
import pandas as pd

with open('models/model.pkl','rb') as f:
    model = pickle.load(f)

# Adding Model version
MODEL_VERSION = '1.0.0'

# getting class labels
class_labels = model.classes_.tolist()
def predict_output(user_input:dict):

    df = pd.DataFrame([user_input])
    predicted_class  = model.predict(df)[0]
    
    # probabilities
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))
    output = {
        "predictied_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilites": class_probs
    }
    return output