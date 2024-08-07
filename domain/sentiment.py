import joblib

class SentimentModel:
    def __init__(self, model_path='models/sentiment_model.pkl'):
        self.model = joblib.load(model_path)
    
    def predict(self, text):
        return self.model.predict([text])[0]
