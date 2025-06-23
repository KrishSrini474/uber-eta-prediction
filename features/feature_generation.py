
def extract_features(event):
    return {
        "pickup_h3": event["pickup_h3"],
        "hour_bin": event["hour_bin"],
        "traffic_score": event["traffic_score"]
    }
