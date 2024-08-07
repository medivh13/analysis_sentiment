# Sentiment Analysis API

This project is a simple implementation of sentiment analysis using Python. The program trains a machine learning model on a given dataset and provides an API to predict the sentiment of a text.

## Folder Structure

analysis_sentiment/
│
├── app.py
├── requirements.txt
├── domain/
│ ├── sentiment_model.py
├── services/
│ ├── sentiment_service.py
├── controllers/
│ ├── sentiment_controller.py
├── models/
│ ├── train_model.py
└── data/
└── dataset.csv


## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/username/sentiment_analysis.git
   cd sentiment_analysis

2. python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows

3. Install dependencies: 
    pip install -r requirements.txt

4. Training the Model
    Ensure the dataset is available in the data directory with the name dataset.csv in the following format:
    Id,Sentiment,Text
    1,negative,<USERNAME> TOLOL!! Gak ada hubungan nya keguguran dgn pake hijab syar'i yg lo bilang bayi nya kepanasan didalem gak ada hubungan nya woyyyy!! Otak sama jempol lo gak singkron sih ya jadinya asal nulis komentar!
    2,negative,Geblek lo tata...cowo bgt dibela2in balikan...hadeww...ntar ditinggal lg nyalahin tuh cowo...padahal kitenya yg oon....

5. Run the script to train the model:
    python3 models/train_model.py

## Running the Application
> Run the Flask application:

- bash
- python3 app.py
- The API will be available at http://127.0.0.1:5000/api.

## Testing the API
- Use tools like Postman or curl to test the API. Here is an example using curl:
- curl -X POST http://127.0.0.1:5000/api/predict -H "Content-Type: application/json" -d

The response will be a JSON containing the text sent and the predicted sentiment.

## Code Structure
- app.py: Main file to run the Flask application.
- domain/sentiment_model.py: Contains the SentimentModel class that loads and uses the model for prediction.
- services/sentiment_service.py: Contains the SentimentService class that uses SentimentModel for sentiment analysis.
- controllers/sentiment_controller.py: Contains the route for the Flask API.
- models/train_model.py: Script to train the model and save it.

## Dependencies
- Flask
- scikit-learn
- pandas
- joblib



