
import random

def generate_json_event():
    return {
        "pickup_lat": random.uniform(12.9, 13.1),
        "pickup_lng": random.uniform(77.5, 77.7),
        "hour_bin": random.randint(0, 23),
        "traffic_score": random.uniform(1, 5)
    }
