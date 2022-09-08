#!/usr/bin/python3
"""This module holds class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel

    Public class attr
        state_id (str):
        name (str):
    """
    state_id = ""
    name = ""
