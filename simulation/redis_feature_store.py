
redis_store = {}

def update_feature_store(trip_id, features):
    redis_store[trip_id] = features

def get_features(trip_id):
    return redis_store.get(trip_id, {})
