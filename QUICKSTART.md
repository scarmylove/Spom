# SPOMS MongoDB Edition - Quick Start

## What is SPOMS?

SPOMS (Supplier and Purchase Order Management System) is a Flask-based web application for managing suppliers, purchase orders, and payments. This is the **MongoDB Edition** - a complete rewrite using MongoDB instead of JSON files for data persistence.

## Key Improvements Over JSON Version

✅ **Scalability** - Handle larger datasets efficiently
✅ **Performance** - Faster queries with indexing
✅ **Reliability** - ACID transactions and data integrity
✅ **Flexibility** - NoSQL schema for easier changes
✅ **Cloud-Ready** - Works with MongoDB Atlas
✅ **Same Features** - All original functionality preserved

## ⚡ Quick Start (5 minutes)

### Step 1: Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 2: Setup MongoDB

**Option A: Using MongoDB Locally**
```bash
# Windows: Download from https://www.mongodb.com/try/download/community
# macOS: brew install mongodb-community && brew services start mongodb-community
# Linux: sudo apt-get install -y mongodb
```

**Option B: Using MongoDB Atlas (Cloud - No Install Needed)**
1. Go to https://www.mongodb.com/cloud/atlas
2. Create free account and cluster
3. Copy connection string

### Step 3: Configure Connection

Edit `.env` file:
```
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=spoms
```

Or for MongoDB Atlas:
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGODB_DB_NAME=spoms
```

### Step 4: Run Application
```bash
python app.py
```

### Step 5: Login
Open http://127.0.0.1:5000 and login with:
- **Username**: dennis
- **Password**: lopez

---

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| **SETUP_GUIDE.md** | Detailed setup instructions |
| **README_MONGODB.md** | Technical architecture & API docs |
| **TESTING_CHECKLIST.md** | Feature verification checklist |
| **MIGRATION_SUMMARY.md** | Complete migration details |
| **setup.sh** | Automated setup script (Unix/Mac/Linux) |

---

## 👥 Demo Accounts

| Role | Username | Password |
|------|----------|----------|
| Administrator | dennis | lopez |
| Purchasing Officer | jani | jani |
| Finance Officer | angel | angel |
| Store Owner | jennifer | jennifer |

---

## 🗂️ File Structure

```
SPOMS-Vercel/
├── app.py                          # Main Flask application
├── db.py                           # MongoDB connection module
├── config.py                       # Flask configuration
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (create from .env.example)
├── .env.example                   # Configuration template
├── setup.sh                       # Setup script
├── migrate_json_to_mongodb.py     # Migration tool (if upgrading)
├── SETUP_GUIDE.md                 # Setup instructions
├── README_MONGODB.md              # Technical documentation
├── TESTING_CHECKLIST.md           # Testing guide
├── MIGRATION_SUMMARY.md           # Migration details
├── data/                          # JSON data files (if upgrading)
├── static/                        # CSS, JavaScript, images
│   ├── css/
│   ├── js/
│   └── images/
└── templates/                     # HTML templates
```

---

## 🚀 Common Tasks

### Run Application
```bash
python app.py
```

### Access Application
http://127.0.0.1:5000

### Migrate from JSON Files
```bash
python migrate_json_to_mongodb.py
```

### Stop Application
Press `Ctrl+C` in terminal

### Install New Dependencies
```bash
pip install -r requirements.txt
```

### Check MongoDB Connection
```bash
python -c "from db import db; print('Connected!' if db else 'Failed')"
```

---

## 🔐 Demo Credentials

### Administrator Account
- **Username**: dennis
- **Password**: lopez
- **Role**: Full system access

### Other Demo Accounts
```
Purchasing Officer: jani / jani
Finance Officer: angel / angel
Store Owner: jennifer / jennifer
```

---

## 📦 Database Collections

Automatically created and initialized:

1. **users** - User accounts (4 demo users)
2. **suppliers** - Supplier information
3. **orders** - Purchase orders
4. **payments** - Payment records
5. **feedback** - User feedback
6. **settings** - System configuration

---

## ✨ Features

### Supplier Management
- View all suppliers
- Add new suppliers
- Edit supplier information
- Delete suppliers

### Order Management
- Create purchase orders
- Track order status
- Update order information
- Monitor deliveries

### Payment Processing
- Record payments
- Track payment status
- Payment history
- Payment methods

### User Management
- Create/edit users
- Assign roles
- User profiles
- Password management

### Reporting
- Sales statistics
- Supplier analytics
- Payment summaries
- Order tracking

### System
- Dashboard overview
- Settings management
- Backup data export
- User feedback

---

## 🛠️ Troubleshooting

### MongoDB Not Connecting
```
Check:
1. MongoDB service is running
2. .env has correct MONGODB_URI
3. For Atlas: IP is whitelisted
4. No firewall blocking port 27017 (local) or 443 (Atlas)
```

### Port 5000 Already in Use
```bash
# Edit app.py last line:
app.run(debug=True, port=5001)
```

### Module Import Error
```bash
pip install --upgrade -r requirements.txt
```

### See detailed troubleshooting in SETUP_GUIDE.md

---

## 📊 Next Steps

1. **Test**: Login with demo account and explore features
2. **Configure**: Customize system settings
3. **Import**: If upgrading, run migration script
4. **Deploy**: Move to production when ready
5. **Backup**: Set up regular MongoDB backups

---

## 🔗 Resources

- [MongoDB Documentation](https://docs.mongodb.com/)
- [PyMongo Guide](https://pymongo.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

---

## 📝 Version Info

- **Application**: SPOMS v2.0 (MongoDB Edition)
- **Python**: 3.8+
- **Database**: MongoDB 4.0+
- **Framework**: Flask 2.3.2
- **Status**: Production Ready

---

## ✅ Getting Help

1. Read **SETUP_GUIDE.md** for detailed instructions
2. Check **TESTING_CHECKLIST.md** to verify setup
3. Review **README_MONGODB.md** for technical details
4. See error messages in terminal output
5. Check MongoDB logs for database issues

---

**Ready to get started?** → Run `python app.py` now!

For detailed setup instructions, see **SETUP_GUIDE.md**
