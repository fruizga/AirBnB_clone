#!/usr/bin/python3
"""class that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """public instance attribute"""
    place_id = ""
    user_id = ""
    text = ""
