import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Flask configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'spoms-secret-key-change-in-production-2026'
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_HTTPONLY = True
    
    # Security: Enable secure cookies only on HTTPS (Vercel always uses HTTPS)
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    if FLASK_ENV == 'production':
        SESSION_COOKIE_SECURE = True
        SESSION_COOKIE_SAMESITE = 'Strict'
    else:
        SESSION_COOKIE_SECURE = False  # Allow HTTP in development
        SESSION_COOKIE_SAMESITE = 'Lax'
    
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # MongoDB configuration
    MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017')
    MONGODB_DB_NAME = os.environ.get('MONGODB_DB_NAME', 'spoms')
    
    # Production settings
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False if FLASK_ENV == 'production' else True