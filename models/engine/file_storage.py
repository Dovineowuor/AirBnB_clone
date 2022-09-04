#!/usr/bin/python3
"""This module holds the class FileStorage"""
import json


class FileStorage():
    """Class FileStorage serializes instances to a
    JSON file and deserializes JSON file to instances
    Private class attributes:
        __file_path (str): path to the JSON file
                     (ex: file.json)
        __objects (dict): empty but will store all
                    objects by <class name>.id
                    (ex: to store a BaseModel object
                    with id=12121212,
                    the key will be BaseModel.12121212)
    Public instance methods:
    all(self):
    new(self, obj):
    save(self):
    reload(self):
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)"""
        dic = {k: v.to_dict() for k, v
               in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If
        the file doesn’t exist, no exception should be raised)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objs = json.load(f)
            for k, v in objs.items():
                cls_name = k.split('.')[0]
                obj = eval(cls_name + "(**v)")
                FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
