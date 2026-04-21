from dataclasses import dataclass

@dataclass
class BoundingBox:
    """
    Define a geographically referenced rectangular region
    """
    min_lat: float
    max_lat: float
    min_lon: float
    max_lon: float
