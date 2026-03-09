#!/usr/bin/env python3
"""schools by topic"""

def schools_by_topic(mongo_collection, topic):
    """find schools"""
    return mongo_collection.find({"topics": topic})

