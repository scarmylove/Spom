# SPOMS - Supplier and Purchase Order Management System (MongoDB Edition)

## Members

- Dennis Lopez Jr
- John Lester Poquita
- Angel Rose Cepe
- Jennifer Urboda

A Flask-based Supplier and Purchase Order Management System built to manage suppliers, purchase orders, payments, and reports using **MongoDB** for data storage.

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB Server (local or cloud)
- pip (Python package manager)

### Installation Steps

1. **Clone/Download the project:**
   ```bash
   cd SPOMS-Vercel
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB:**
   - Create a `.env` file in the project root (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```
   
   - Edit `.env` with your MongoDB connection details:
   ```
   MONGODB_URI=mongodb://localhost:27017
   MONGODB_DB_NAME=spoms
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-change-in-production-2026
   ```

   **For MongoDB Cloud (Atlas)**, use:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
   ```

4. **Start MongoDB:**
   - **Local MongoDB:**
     ```bash
     mongod
     ```
   - **Or use MongoDB Atlas** (cloud-based, no local setup needed)

5. **Run the application:**
   ```powershell
   python app.py
   ```

6. **Open in browser:**
   ```
   http://127.0.0.1:5000
   ```

## Demo Accounts

| Role | Username | Password |
|------|----------|----------|
| Admin | dennis | lopez |
| Purchasing Officer | jani | jani |
| Finance Officer | angel | angel |
| Store Owner | jennifer | jennifer |

## Key Features

### Module 1: Supplier Management
- Add, view, update, and delete suppliers
- Search suppliers by text and status
- Manage supplier contact information

### Module 2: Purchase Order Management
- Create purchase orders with supplier selection
- Automatic subtotal and total computation
- Track order status (Pending, Approved, Delivered, Cancelled)
- Update order details and delivery dates

### Module 3: Delivery & Receiving
- Track delivery status through order management
- Record expected and actual delivery dates
- Monitor order completion

### Module 4: Payment Management
- Record supplier payments
- Select payment methods (Bank Transfer, Check, Cash)
- Update payment status (Pending, Partial, Paid)
- Track payment balance

### Module 5: Reporting
- Generate purchase order reports
- View payment summaries
- Export data to CSV
- Interactive dashboard with charts

## Database Structure

### Collections in MongoDB

- **users** - User accounts with roles
- **suppliers** - Supplier information
- **orders** - Purchase orders
- **payments** - Payment records
- **feedback** - User feedback
- **settings** - System configuration

## Architecture Changes from JSON to MongoDB

### Previous (JSON):
```python
def load_json(f):
    # Read from data/file.json

def save_json(f, d):
    # Write to data/file.json
```

### Current (MongoDB):
```python
def get_collection(collection_name):
    # Connect to MongoDB collection

db.collection.find()      # Read
db.collection.insert_one()  # Write
db.collection.update_one()  # Update
db.collection.delete_one()  # Delete
```

## File Structure

```
SPOMS-Vercel/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── db.py                 # MongoDB connection & initialization
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Environment variables (create from template)
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript modules
│   └── images/           # Uploaded images
└── templates/            # HTML templates
```

## Configuration

Edit `.env` to change:
- MongoDB connection URI
- Database name
- Flask environment
- Secret key

## Error Handling

If MongoDB connection fails:
1. Verify MongoDB is running
2. Check `.env` configuration
3. Check network connectivity (for MongoDB Atlas)
4. Review logs in the console

## Performance Tips

- MongoDB automatically creates indexes on common fields
- Users and suppliers have unique indexes on `username` and `id`
- Orders indexed by `po` number for faster lookups

## Migration from JSON

If migrating from JSON storage:
1. Install MongoDB
2. Update `.env` with MongoDB connection
3. Run `python app.py` to initialize collections
4. Manually migrate data using MongoDB CLI or custom migration script

## Development

To enable debug mode, set in `.env`:
```
FLASK_ENV=development
```

## Security Notes

- Change `SECRET_KEY` in production
- Set `SESSION_COOKIE_SECURE=True` for HTTPS
- Use strong passwords for MongoDB
- Implement rate limiting for production
- Keep dependencies updated

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB service is running
- Check connection string in `.env`
- Verify firewall settings

### Collections Not Created
- Application auto-creates collections on first run
- Check console for initialization messages

### Import Errors
- Run `pip install -r requirements.txt`
- Verify Python 3.8+

## Support

For issues or questions, contact the development team or refer to Flask and PyMongo documentation.

---

**Last Updated:** April 2026  
**Version:** 2.0 (MongoDB Edition)
