from typing import Any, Dict, List, Optional
from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDAL:
    """Handles MongoDB Atlas connection."""

    def __init__(self):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]

    def get_collection(self):
        return


class MongoQueryBuilder:
    """Fluent API for building MongoDB queries."""

    def __init__(self):


    def add_filter(self):
        mongo_ops = {
            "eq": "$eq", "ne": "$ne", "gt": "$gt", "gte": "$gte",
            "lt": "$lt", "lte": "$lte", "in": "$in", "nin": "$nin",
            "exists": "$exists", "type": "$type", "regex": "$regex",
            "all": "$all", "size": "$size"
        }


    def add_elem_match(self):
        
        return self

    def add_or_condition(self):

        return self

    def set_sort(self):

        return self

    def set_limit(self):

        return self

    def set_skip():

        return self

    def set_projection(self):

        return self

    def execute(self)
        return list()