from collections import Counter

def find_hotspots(accident_zones: list):
    """
    Finds accident-prone zones based on frequency.
    """

    zone_counts = Counter(accident_zones)

    hotspots = []

    for zone, count in zone_counts.items():
        hotspots.append({
            "zone": zone,
            "accident_count": count
        })

    # Sort hotspots by highest accidents
    hotspots = sorted(hotspots, key=lambda x: x["accident_count"], reverse=True)

    return hotspots
