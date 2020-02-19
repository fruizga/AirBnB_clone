#!/usr/bin/python3
"""class that inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
