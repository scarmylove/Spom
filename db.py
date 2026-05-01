"""MongoDB Database Connection and Operations"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME', 'Spoms')  # KEEP CASE CONSISTENT

client = None
db = None

def connect_db():
    global client, db
    if client is None:
        try:
            client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
            client.admin.command('ping')
            db = client[MONGODB_DB_NAME]
            print("✓ Connected to MongoDB successfully")
        except ConnectionFailure:
            print("✗ Failed to connect to MongoDB")
            db = None

def get_db():
    if db is None:
        connect_db()
    return db

def get_collection(collection_name):
    database = get_db()
    if database is None:
        raise ConnectionError("MongoDB connection failed")
    return database[collection_name]


def init_db():
    """Run this ONLY ONCE manually"""
    database = get_db()
    if database is None:
        return

    collections = ['users', 'suppliers', 'orders', 'payments', 'feedback', 'settings']
    existing = database.list_collection_names()

    for col in collections:
        if col not in existing:
            database.create_collection(col)

    # Indexes
    database.users.create_index('username', unique=True, sparse=True)
    database.suppliers.create_index('id', unique=True)
    database.orders.create_index('po', unique=True)
    database.payments.create_index('id', unique=True)

    # Default settings
    if database.settings.count_documents({}) == 0:
        database.settings.insert_one({
            'system_name': 'SPOMS',
            'logo': 'images/logo.png',
            'homepage_background': 'images/spoms.png'
        })

    # Default users
    if database.users.count_documents({}) == 0:
        database.users.insert_many([
            {
                "user_id": "U001",
                "name": "Dennis Lopez Jr",
                "username": "dennis",
                "password": "0e66633604475ead7445c5e5f987d6450c23687eccf37665e3924541a7f8f6b3",
                "role": "Administrator",
                "email": "dennis@spoms.com",
                "status": "Active"
            }
        ])
