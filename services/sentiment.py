from domain.sentiment import SentimentModel

class SentimentService:
    def __init__(self):
        self.model = SentimentModel()
    
    def analyze_sentiment(self, text):
        return self.model.predict(text)
