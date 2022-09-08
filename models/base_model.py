#!/usr/bin/python3
"""This module holds class BaseModel
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Basemodel is parent class that defines
    all common attributes/methods for other classes

    Public instance attributes:
        id (str): assigns with an uuid when an instance is created
        created_at (datetime): assigns with the current datetime
                               when an instance is created
        updated_at (datetime): assigns with the current datetime
                               when an instance is created and it
                               will be updated every time you change your
                               object
    Public instance methods:
        save(self):
        to_dict(self):
    """
    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        temp = dict(self.__dict__)
        temp["updated_at"] = self.__dict__["updated_at"].isoformat()
        temp["created_at"] = self.__dict__["created_at"].isoformat()
        temp["__class__"] = self.__class__.__name__
        return temp

    def __str__(self):
        """Makes class printable"""
        string = "[{}] ".format(self.__class__.__name__)
        string += "({}) {}".format(self.id, self.__dict__)
        return string
