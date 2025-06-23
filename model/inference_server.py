
def predict(model, pickup_h3, hour_bin, traffic_score):
    return model(pickup_h3, hour_bin, traffic_score)
