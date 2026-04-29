"""
MongoDB Database Connection and Operations (Vercel-safe version)
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "spoms")

client = None
db = None
_connected = False


# -------------------------------
# CONNECTION (SAFE / LAZY)
# -------------------------------
def connect_db():
    global client, db, _connected

    if _connected:
        return db

    if not MONGODB_URI:
        print("✗ MongoDB URI not found in environment variables")
        return None

    try:
        client = MongoClient(
            MONGODB_URI,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
        )

        client.admin.command("ping")

        db = client[MONGODB_DB_NAME]
        _connected = True

        print("✓ MongoDB Connected Successfully")
        return db

    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        print("✗ MongoDB Connection Failed:", e)
        db = None
        _connected = False
        return None


# -------------------------------
# GET DB
# -------------------------------
def get_db():
    return connect_db()


# -------------------------------
# GET COLLECTION
# -------------------------------
def get_collection(collection_name):
    database = connect_db()

    if database is None:
        raise ConnectionError("MongoDB connection failed")

    return database[collection_name]


# -------------------------------
# INIT DATABASE (SAFE)
# -------------------------------
def init_db():
    database = connect_db()

    if database is None:
        print("⚠ Skipping DB initialization (no connection)")
        return

    collections = [
        "users",
        "suppliers",
        "orders",
        "payments",
        "feedback",
        "settings",
    ]

    # Create collections if missing
    for name in collections:
        if name not in database.list_collection_names():
            database.create_collection(name)
            print(f"✓ Created collection: {name}")

    # Indexes
    database.users.create_index("username", unique=True, sparse=True)
    database.suppliers.create_index("id", unique=True)
    database.orders.create_index("po", unique=True)
    database.payments.create_index("id", unique=True)

    # -------------------------------
    # DEFAULT SETTINGS
    # -------------------------------
    if database.settings.count_documents({}) == 0:
        database.settings.insert_one({
            "system_name": "SPOMS",
            "logo": "images/logo.png",
            "homepage_background": "images/spoms.png"
        })
        print("✓ Default settings created")

    # -------------------------------
    # DEFAULT USERS (KEEP YOUR USERS)
    # -------------------------------
    if database.users.count_documents({}) == 0:
        default_users = [
            {
                "user_id": "U001",
                "name": "Dennis Lopez Jr",
                "username": "dennis",
                "password": "0e66633604475ead7445c5e5f987d6450c23687eccf37665e3924541a7f8f6b3",
                "role": "Administrator",
                "email": "dennis@spoms.com",
                "status": "Active"
            },
            {
                "user_id": "U002",
                "name": "Jani",
                "username": "jani",
                "password": "dd8a3af07bf0ed457e80ebfa07a8d2a7d834bb30aaee2cbf97d3b6120e6238b8",
                "role": "Purchasing Officer",
                "email": "jani@spoms.com",
                "status": "Active"
            },
            {
                "user_id": "U003",
                "name": "Angel Rose Cepe",
                "username": "angel",
                "password": "519ba91a5a5b4afb9dc66f8805ce8c442b6576316c19c6896af2fa9bda6aff71",
                "role": "Finance Officer",
                "email": "angel@spoms.com",
                "status": "Active"
            },
            {
                "user_id": "U004",
                "name": "Jennifer Urboda",
                "username": "jennifer",
                "password": "9ce8db922a8f4a7abd859adee70bd8b7a63321265487da54cf4bed6a69eb3e1b",
                "role": "Store Owner",
                "email": "jennifer@spoms.com",
                "status": "Active"
            }
        ]

        database.users.insert_many(default_users)
        print("✓ Default users inserted")


# Auto-connect when imported (safe lightweight check)
connect_db()
