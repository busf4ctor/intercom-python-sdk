from uplink import Consumer

from .admins.api import AdminsAPI
from ..core.api_base import APIBase

class TagsToAPI(dict):
    allowed_types = (APIBase, Consumer) 

    def __setitem__(self, key, value):
        if not isinstance(value, self.allowed_types):
            raise TypeError(f"Invalid type. Value must be one of types {TagsToAPI.allowed_types}.")
        super().__setitem__(key, value)


tags_to_api_dict = TagsToAPI()
tags_to_api_dict["admins"] = AdminsAPI