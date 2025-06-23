
import torch
from torch.utils.data import DataLoader, TensorDataset
from eta_model import ETAModel

def train_model(X, y, epochs=10):
    model = ETAModel()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    dataset = TensorDataset(*X, y)
    loader = DataLoader(dataset, batch_size=16, shuffle=True)

    for epoch in range(epochs):
        for xb, yb in loader:
            pred = model(*xb)
            loss = criterion(pred.squeeze(), yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
    return model
