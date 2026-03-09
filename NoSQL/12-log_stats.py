#!/usr/bin/env python3
"""nginx logs stats"""

from pymongo import MongoClient


def main():
    """print stats"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx

    total = col.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        count = col.count_documents({"method": m})
        print(f"	method {m}: {count}")

    status = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    main()

