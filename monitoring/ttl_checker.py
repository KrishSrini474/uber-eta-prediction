
import time

def is_fresh(timestamp, ttl=300):
    return (time.time() - timestamp) < ttl
