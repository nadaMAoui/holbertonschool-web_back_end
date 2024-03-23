import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["logs"]
collection = db["nginx"]

# Get total number of documents
total_logs = collection.count_documents({})

# Get method counts
method_counts = collection.aggregate([
    {"$group": {"_id": "$method", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
])

# Get count for method=GET, path=/status
status_count = collection.count_documents({"method": "GET", "path": "/status"})

# Print results
print(f"{total_logs} logs")
print("Methods:")
for method_count in method_counts:
    print(f"\t{method_count['count']} {method_count['_id']}")
print(f"\t{status_count} GET /status")

# Close MongoDB connection
client.close()
