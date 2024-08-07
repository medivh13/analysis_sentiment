from flask import Blueprint, request, jsonify
from services.sentiment import SentimentService

sentiment_blueprint = Blueprint('sentiment', __name__)
service = SentimentService()

@sentiment_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    sentiment = service.analyze_sentiment(text)
    
    response = {
        'text': text,
        'sentiment': sentiment
    }
    
    return jsonify(response)
