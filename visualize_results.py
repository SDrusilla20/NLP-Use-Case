
import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from dnn_classifier import QoSModel

# Load data and model
df = pd.read_csv('noisy_stream_data_with_sentiment.csv')

# Binarize satisfaction score for classification (>=0.5 = satisfied)
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

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Unsatisfied", "Satisfied"])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix for Satisfaction Prediction")
plt.savefig("confusion_matrix.png")  # Add this line before plt.show()
plt.show()
