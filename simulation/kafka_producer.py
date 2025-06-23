
import time
import json
import random

def generate_event():
    return {
        "trip_id": random.randint(1000, 9999),
        "pickup_h3": f"h3_{random.randint(1, 100)}",
        "dropoff_h3": f"h3_{random.randint(1, 100)}",
        "hour_bin": random.randint(0, 23),
        "driver_id": random.randint(1, 10),
        "traffic_score": round(random.uniform(0.5, 3.0), 2)
    }

def produce_events(n=10):
    for _ in range(n):
        event = generate_event()
        print("Produced event:", json.dumps(event))
        time.sleep(1)

if __name__ == "__main__":
    produce_events()
