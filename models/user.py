#!/usr/bin/python3
"""This module holds class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel

    Public class attr
        email (str):
        password (str):
        first_name (str):
        last_name (stir):
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
