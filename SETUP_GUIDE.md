# SPOMS MongoDB Edition - Setup Guide

## Prerequisites

- Python 3.8 or higher
- MongoDB (local or MongoDB Atlas cloud account)
- pip (Python package manager)

## Step 1: Install MongoDB

### Option A: Local MongoDB Installation

**Windows:**
1. Download MongoDB Community from: https://www.mongodb.com/try/download/community
2. Run the installer and follow the installation wizard
3. MongoDB will start as a Windows service automatically

**macOS:**
```bash
brew install mongodb-community
brew services start mongodb-community
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install -y mongodb
sudo systemctl start mongodb
```

### Option B: MongoDB Atlas (Cloud)

1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a new cluster (free tier available)
4. Create a database user
5. Get your connection string (looks like: `mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/`)

## Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Flask 2.3.2
- Werkzeug 2.3.6
- PyMongo 4.4.1
- python-dotenv 1.0.0

## Step 3: Configure Environment Variables

1. Open `.env` file (or copy from `.env.example` if it doesn't exist)

2. Configure MongoDB connection:

**For Local MongoDB:**
```
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=spoms
FLASK_ENV=development
SECRET_KEY=your-secret-key-change-in-production-2026
```

**For MongoDB Atlas:**
```
MONGODB_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/
MONGODB_DB_NAME=spoms
FLASK_ENV=development
SECRET_KEY=your-secret-key-change-in-production-2026
```

## Step 4: Run the Application

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

## Step 5: Access the Application

Open your browser and go to: http://127.0.0.1:5000

### Demo Accounts

| Role | Username | Password |
|------|----------|----------|
| Administrator | dennis | lopez |
| Purchasing Officer | jani | jani |
| Finance Officer | angel | angel |
| Store Owner | jennifer | jennifer |

## Step 6: Data Migration (Optional)

If you have existing JSON data from the previous version:

1. Ensure MongoDB is running and .env is configured
2. Run the migration script:
   ```bash
   python migrate_json_to_mongodb.py
   ```
3. The script will:
   - Create a backup of JSON files in `data_backup_YYYYMMDD_HHMMSS/`
   - Transfer all data to MongoDB collections
   - Show migration summary

## Database Collections

The application automatically creates these collections on startup:

| Collection | Purpose |
|-----------|---------|
| users | User accounts and authentication |
| suppliers | Supplier information |
| orders | Purchase orders |
| payments | Payment records |
| feedback | User feedback |
| settings | System configuration |

## Troubleshooting

### MongoDB Connection Error
- Check `.env` file has correct MONGODB_URI
- Verify MongoDB server is running
- For MongoDB Atlas, ensure IP is whitelisted in cluster settings

### Import Error: "No module named 'pymongo'"
```bash
pip install pymongo
```

### Port Already in Use
Change the port in app.py:
```python
app.run(debug=True, port=5001)
```

### Database Already Exists
If you get "database already exists" error, the collections will be created on first access. This is normal.

## Features Available

✓ User Management (Create, Read, Update, Delete users)
✓ Supplier Management
✓ Purchase Order Management
✓ Payment Management
✓ Feedback System
✓ Reports and Analytics
✓ Dashboard with statistics
✓ Role-based access control
✓ Settings management
✓ User profile management

## Security Notes

- Change `SECRET_KEY` in `.env` for production
- For production, set `FLASK_ENV=production`
- Enable `SESSION_COOKIE_SECURE=True` for HTTPS
- Use strong MongoDB passwords
- Regular backups are recommended

## Performance Tips

- Create indexes on frequently queried fields
- Use connection pooling for high traffic
- Monitor MongoDB logs for slow queries
- Consider MongoDB sharding for large datasets

## Support

For issues or questions:
1. Check the README_MONGODB.md for detailed documentation
2. Review application logs for error messages
3. Verify MongoDB connection and permissions
4. Ensure all required packages are installed

## Next Steps

1. Test all features with demo accounts
2. Create your own users
3. Import existing data if needed
4. Configure backup strategy
5. Plan for production deployment
