
def should_retrain(drift_score, threshold=0.1):
    return drift_score > threshold
