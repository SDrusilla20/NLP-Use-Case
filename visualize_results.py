
import pandas as pd
import torch
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from dnn_classifier import QoSModel
from sklearn.metrics import accuracy_score



# Load data and model
df = pd.read_csv('noisy_stream_data_with_sentiment.csv')
df['satisfaction_binary'] = df['satisfaction'].apply(lambda x: 1 if x >= 0.5 else 0)

le_network = LabelEncoder().fit(df['network'])
le_quality = LabelEncoder().fit(df['quality'])
le_sentiment = LabelEncoder().fit(df['sentiment'])

X = df[['network', 'quality', 'sentiment']].copy()
X['network'] = le_network.transform(X['network'])
X['quality'] = le_quality.transform(X['quality'])
X['sentiment'] = le_sentiment.transform(X['sentiment'])

X_tensor = torch.tensor(X.values, dtype=torch.float32)

model = QoSModel()
model.load_state_dict(torch.load('qos_model.pth'))
model.eval()

with torch.no_grad():
    predictions = model(X_tensor).squeeze().numpy()

# Convert predictions to binary
y_pred = (predictions >= 0.5).astype(int)
y_true = df['satisfaction_binary'].values

accuracy = accuracy_score(y_true, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Unsatisfied", "Satisfied"])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix for Satisfaction Prediction")
plt.savefig("confusion_matrix.png")
plt.show()

sentiment_counts = df['sentiment'].value_counts().to_dict()

# Save sentiment counts to a JSON file
with open('sentiment_counts.json', 'w') as f:
    json.dump(sentiment_counts, f)

# Visualization of the sentiment distribution 
labels = list(sentiment_counts.keys())
values = list(sentiment_counts.values())

fig, ax = plt.subplots()
ax.bar(labels, values, color=['#4CAF50', '#FFC107', '#F44336'])
ax.set_ylabel('Counts')
ax.set_title('Sentiment Distribution')

plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()