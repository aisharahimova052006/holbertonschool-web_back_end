#!/usr/bin/env python3
"""mongo"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """using find to list all documents"""
    listed = mongo_collection.find({})
    return listed
