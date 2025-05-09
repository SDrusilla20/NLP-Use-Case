import pandas as pd
from transformers import pipeline

# Load the 3-class sentiment analysis model
classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Label mapping
label_map = {
    'LABEL_0': 'Negative',
    'LABEL_1': 'Neutral',
    'LABEL_2': 'Positive'
}

# Load dataset
df = pd.read_csv('noisy_stream_data.csv')

# Apply sentiment classification with label mapping
df['sentiment'] = df['comment'].apply(lambda x: label_map[classifier(x)[0]['label']])

# Save the new dataset
df.to_csv('noisy_stream_data_with_sentiment.csv', index=False)

print("Sentiment analysis completed.")
