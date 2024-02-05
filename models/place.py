#!/usr/bin/python3

"""
Module containing Place class, incorporating data from all other classes
"""
from .base_model import BaseModel



class Place(BaseModel):
    """
    Place class, inheriting from BaseModel and utilizing sibling classes

    Attributes:
        city_id: string - the id of the City a Place is located in
        user_id: string - the id of the User listing the Place
        name: string - the name of the Place
        Description: string - a brief description of the Place
        number_rooms: integer - the number of rooms the Place has
        number_bathrooms: integer - the number of bathrooms the Place has
        max_guest: integer - the maximum number of guests a Place can have
        at once
        price_by_night: integer - the price of the Place per night
        latitude: float - the latitude of the Place
        longitutde: float - the longitude of the Place
        amenity_ids: list - a list of ids for various Amenities that the Place
        has
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        super().__init__()
