#!/usr/bin/python3
"""This module defines class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Public class attr
        city_id (str) default=empty string: it will be the City.id
        user_id (str) default=empty string: it will be the User.id
        name (str) default=empty string:
        description (str) default=empty string:
        number_rooms (int) default=0:
        number_bathrooms (int) default=0:
        max_guest (int) default=0:
        price_by_night (int): 0
        latitude (float) default=0.0:
        longitude (float) default=0.0:
        amenity_ids (list of string) default=empty list:
            it will be the list of Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
