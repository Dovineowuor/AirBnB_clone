#!/usr/bin/python3
"""This module defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attr
        place_id (str) default=empty string: it will be the Place.id
        user_id (str) default=empty string: it will be the User.id
        text (str) default=empty string:
    """
    place_id = ""
    user_id = ""
    text = ""
