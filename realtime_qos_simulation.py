import torch
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from dnn_classifier import QoSModel

# Load encoders and model
df = pd.read_csv('noisy_stream_data_with_sentiment.csv')
le_network = LabelEncoder().fit(df['network'])
le_quality = LabelEncoder().fit(df['quality'])
le_sentiment = LabelEncoder().fit(df['sentiment'])

model = QoSModel()
model.load_state_dict(torch.load('qos_model.pth'))
model.eval()

# Simulate input
sample = {
    'network': 'Moderate',
    'quality': '720p',
    'sentiment': 'NEGATIVE'
}

sample_enc = torch.tensor([[
    le_network.transform([sample['network']])[0],
    le_quality.transform([sample['quality']])[0],
    le_sentiment.transform([sample['sentiment']])[0],
]], dtype=torch.float32)

with torch.no_grad():
    prediction = model(sample_enc).item()
    action = "Maintain" if prediction >= 0.5 else "Adjust bitrate or resolution"
    print(f"Predicted satisfaction: {prediction:.2f} → Suggested action: {action}")
