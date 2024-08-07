import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def train_model():
    df = pd.read_csv('data/dataset.csv')
    df = df[['Sentiment', 'Text']]
    
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(df['Text'], df['Sentiment'])
    
    joblib.dump(model, 'models/sentiment_model.pkl')

    # Mencetak informasi mengenai data yang ditraining
    total_data = len(df)
    sentiment_counts = df['Sentiment'].value_counts()
    
    print(f"Total data yang ditraining: {total_data}")
    print("Distribusi sentimen:")
    for sentiment, count in sentiment_counts.items():
        print(f"  {sentiment}: {count}")

if __name__ == '__main__':
    train_model()
