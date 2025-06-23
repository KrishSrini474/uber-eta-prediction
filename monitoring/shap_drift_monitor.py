
def monitor_drift(feature_values, baseline_values):
    drift = abs(feature_values.mean() - baseline_values.mean())
    return drift
