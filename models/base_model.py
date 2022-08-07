#!/usr/bin/python3
"""
This model defines all common attribtes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            from models.__init__ import storage
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Print the String representation of the object
        """
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """
        Updates the updated_at value
        """
        self.updated_at = datetime.utcnow()
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing all key/values of
        __dict__ instance
        """
        map_obj = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_obj[key] = value.isoformat()
            else:
                map_obj[key] = value
        map_obj["__class__"] = self.__class__.__name__
        return map_obj
