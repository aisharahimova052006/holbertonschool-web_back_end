#!/usr/bin/env python3
"""insert"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """insert"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id

