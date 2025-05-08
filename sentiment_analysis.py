# sentiment_analysis.py
import pandas as pd
from transformers import pipeline

df = pd.read_csv('noisy_stream_data.csv')
classifier = pipeline('sentiment-analysis')

# Add sentiment using BERT
df['sentiment'] = df['comment'].apply(lambda x: classifier(x)[0]['label'])
df.to_csv('noisy_stream_data_with_sentiment.csv', index=False)
print("Sentiment analysis completed.")
