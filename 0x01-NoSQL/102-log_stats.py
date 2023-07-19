#!/usr/bin/env python3

'''
    A Python module that Provides stats about Nginx logs stored in MongoDB.

    Args: mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns: tuple: A tuple containing the number of logs, a dictionary with the count of each method,
    and a dictionary with the top 10 most present IPs in the logs.
'''



from pymongo import MongoClient

def log_stats(mongo_collection):
   


    num_logs = mongo_collection.count_documents({})
    
    # Get the count of each method
    methods_count = {
        "GET": mongo_collection.count_documents({"method": "GET"}),
        "POST": mongo_collection.count_documents({"method": "POST"}),
        "PUT": mongo_collection.count_documents({"method": "PUT"}),
        "PATCH": mongo_collection.count_documents({"method": "PATCH"}),
        "DELETE": mongo_collection.count_documents({"method": "DELETE"})
    }
    
    # Get the top 10 IPs
    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    
    ips_count = {ip['_id']: ip['count'] for ip in top_ips}
    
    return num_logs, methods_count, ips_count

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    num_logs, methods_count, ips_count = log_stats(logs_collection)

    print(f"{num_logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print("IPs:")
    for ip, count in ips_count.items():
        print(f"\t{ip}: {count}")

