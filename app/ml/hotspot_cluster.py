def identify_hotspots(accident_data):
    """
    Geospatial placeholder logic.
    Later replaced with DBSCAN/KMeans.
    """

    sorted_zones = sorted(
        accident_data,
        key=lambda x: x["count"],
        reverse=True
    )

    return sorted_zones[:3]
