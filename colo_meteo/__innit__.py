"""
Colombian Weather - A library for accessing Colombian meteorological data
"""

from .client import ColombianWeatherClient
from .fence import BoundingBox
from .utils import where_clause

__version__ = "1.0.0"
__author__ = "Parera"
__all__ = [
    'ColombianWeatherClient',
    'BoundingBox',
    'where_clause',
]