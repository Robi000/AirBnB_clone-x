# !/usr/bin/python3

"""this is base class for entire project
"""
from datetime import datetime
from uuid import uuid4
import models

storage = models.storage

DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """this is the main main class which others inherithed from
    """

    def __init__(self, *args, **kwargs):
        """this will aceept args and kwargs and return nothing 
            args: 
                args: not used
                kwargs
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
            # print('_____________')
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                else:
                    self.__dict__[key] = value

    def __str__(self) -> str:
        """return string representation of an object

        Returns:
            str
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update updated at at the moment of edit
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """return dictionary of an instance of an object 

        Returns:
            dictionary : instant representation for json dump =
        """
        ret = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                ret[key] = value.isoformat()
            else:
                ret[key] = value
        ret.update(__class__=self.__class__.__name__)
        return ret

# print(BaseModel)
