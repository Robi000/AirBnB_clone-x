# !/usr/bin/python3

"""this is base class for entire project
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """this is initialiazing the base model with args and kwargs 
        """        
        super().__init__(*args, **kwargs)
