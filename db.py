"""MongoDB Database Connection and Operations"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME', 'Spoms')

try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Verify connection
    client.admin.command('ping')
    db = client[MONGODB_DB_NAME]
    print("✓ Connected to MongoDB successfully")
except ConnectionFailure:
    print("✗ Failed to connect to MongoDB")
    db = None


def get_db():
    """Get database instance"""
    return db


def get_collection(collection_name):
    """Get a collection from the database"""
    if db is None:
        raise ConnectionError("MongoDB connection failed")
    return db[collection_name]


def init_db():
    """Initialize database collections and indexes"""
    if db is None:
        return
    
    # Create collections if they don't exist
    collections = ['users', 'suppliers', 'orders', 'payments', 'feedback', 'settings']
    
    for collection_name in collections:
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"✓ Created collection: {collection_name}")
    
    # Create indexes for better performance
    db.users.create_index('username', unique=True, sparse=True)
    db.suppliers.create_index('id', unique=True)
    db.orders.create_index('po', unique=True)
    db.payments.create_index('id', unique=True)
    
    # Initialize settings if empty
    if db.settings.count_documents({}) == 0:
        db.settings.insert_one({
            'system_name': 'SPOMS',
            'logo': 'images/logo.png',
            'homepage_background': 'images/spoms.png'
        })
        print("✓ Initialized default settings")
    
    # Initialize default users if empty
    if db.users.count_documents({}) == 0:
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
        db.users.insert_many(default_users)
        print("✓ Initialized default users")
