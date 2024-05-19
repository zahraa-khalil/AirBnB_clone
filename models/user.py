#!/usr/bin/python3
"""Defines User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for AirBnB project"""

    def __init__(self, email, password, first_name, last_name):
        """Initialize a new User instance.

        Args:
            email (str): User's email.
            password (str):  User's password.
            first_name (str): User's first name.
            last_name (str): User's last name.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
