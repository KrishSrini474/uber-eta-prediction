
import torch
import torch.nn as nn

class ETAModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.pickup_embedding = nn.Embedding(100, 8)
        self.hour_embedding = nn.Embedding(24, 4)
        self.fc = nn.Sequential(
            nn.Linear(8 + 4 + 1, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, pickup_h3, hour_bin, traffic_score):
        pickup_emb = self.pickup_embedding(pickup_h3)
        hour_emb = self.hour_embedding(hour_bin)
        x = torch.cat([pickup_emb, hour_emb, traffic_score.unsqueeze(1)], dim=1)
        return self.fc(x)
