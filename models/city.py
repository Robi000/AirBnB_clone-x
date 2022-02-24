# !/usr/bin/python3

"""this is class city class for project 
"""
from .base_model import BaseModel


class City(BaseModel):
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """this initialize base with the args and kwargs for base 
        """        
        super().__init__(*args, **kwargs)
