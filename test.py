from pymongo import MongoClient

uri = "mongodb+srv://dennis:Spoms12345@spoms.okvcnfc.mongodb.net/spoms?retryWrites=true&w=majority"

client = MongoClient(
    uri,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000
)

try:
    print("Connecting...")
    client.admin.command("ping")
    print("✓ MongoDB Connected")
except Exception as e:
    print("✗ Failed:", e)