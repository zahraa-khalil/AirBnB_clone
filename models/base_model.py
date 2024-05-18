#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self):
        """Initialize a new Base instance with a unique ID and timestamps."""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
