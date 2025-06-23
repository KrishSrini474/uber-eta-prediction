
def latlng_to_h3(lat, lng, resolution=9):
    return f"h3_{int((lat + lng) * 10) % 100}"
