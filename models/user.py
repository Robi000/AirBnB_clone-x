# !/usr/bin/python3

"""this is class for user model 
"""

from .base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize base model with what we hace args and kwargs 
        """        
        super().__init__(*args, **kwargs)
