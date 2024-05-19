#!/usr/bin/python3
"""Define city Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Initialize a new Amenity instance.

    Args:
        name (str): Amenity's name.
    """
    name = ""
