#!/usr/bin/env python3
"""Module for providing stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def print_nginx_logs_stats():
    """Print stats about Nginx logs."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check
    status_check = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    print_nginx_logs_stats()