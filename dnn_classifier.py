import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import TensorDataset, DataLoader

# Define a simple regression model
class QoSModel(nn.Module):
    def __init__(self):
        super(QoSModel, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
        )

    def forward(self, x):
        return self.model(x)

if __name__ == "__main__":
    # Load and encode data
    df = pd.read_csv('noisy_stream_data_with_sentiment.csv')
    le_network = LabelEncoder()
    le_quality = LabelEncoder()
    le_sentiment = LabelEncoder()

    df['network_enc'] = le_network.fit_transform(df['network'])
    df['quality_enc'] = le_quality.fit_transform(df['quality'])
    df['sentiment_enc'] = le_sentiment.fit_transform(df['sentiment'])

    X = df[['network_enc', 'quality_enc', 'sentiment_enc']].values
    y = df['satisfaction'].values.astype('float32')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert to PyTorch tensors
    train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32),
                                  torch.tensor(y_train, dtype=torch.float32))
    test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32),
                                 torch.tensor(y_test, dtype=torch.float32))

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32)

    model = QoSModel()
    loss_fn = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train the model
    for epoch in range(20):
        model.train()
        total_loss = 0
        for xb, yb in train_loader:
            pred = model(xb).squeeze()
            loss = loss_fn(pred, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

    torch.save(model.state_dict(), 'qos_model.pth')
    print("PyTorch model trained and saved.")
