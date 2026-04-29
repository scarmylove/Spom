# SPOMS - Supplier and Purchase Order Management System
## MongoDB Edition v2.0

**Status**: ✅ Production Ready | **Database**: MongoDB | **Framework**: Flask

---

## 🎯 What is SPOMS?

SPOMS is a comprehensive web-based procurement management system designed for businesses to:
- **Manage Suppliers** - Track supplier information and contacts
- **Create Purchase Orders** - Generate and manage POs efficiently
- **Process Payments** - Record and track payment status
- **Analyze Data** - Generate reports and view analytics
- **Control Access** - Role-based permissions (Admin, PO Officer, Finance, Store Owner)

This is the **MongoDB Edition** - a modern NoSQL implementation replacing the original JSON-based version.

## 👥 Team Members

- Dennis Lopez Jr
- John Lester Poquita
- Angel Rose Cepe
- Jennifer Urboda

---

## 🚀 Quick Start

### Option 1: 5-Minute Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure MongoDB (edit .env)
# For local: MONGODB_URI=mongodb://localhost:27017
# For cloud: MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/

# 3. Run application
python app.py

# 4. Login
# Open http://127.0.0.1:5000
# Username: dennis, Password: lopez
```

**[👉 See QUICKSTART.md for 5-minute setup](QUICKSTART.md)**

### Option 2: Detailed Setup
**[👉 See SETUP_GUIDE.md for comprehensive instructions](SETUP_GUIDE.md)**

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **[INDEX.md](INDEX.md)** | Complete documentation map (START HERE) |
| **[QUICKSTART.md](QUICKSTART.md)** | 5-minute quick start guide |
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | Detailed setup instructions |
| **[README_MONGODB.md](README_MONGODB.md)** | Technical architecture & API docs |
| **[TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)** | Feature verification (20+ tests) |
| **[CHANGELOG.md](CHANGELOG.md)** | What's new in v2.0 |
| **[MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md)** | MongoDB migration details |
| **[COMPLETION_REPORT.md](COMPLETION_REPORT.md)** | Project completion status |

**👉 [Read INDEX.md to find exactly what you need](INDEX.md)**

---

## ✨ Key Features

### Supplier Management
✅ Add and manage suppliers  
✅ Track contact information  
✅ Location and address management  

### Purchase Orders
✅ Create purchase orders  
✅ Track item details and pricing  
✅ Monitor order status  
✅ Manage deliveries  

### Payment Processing
✅ Record payments  
✅ Track payment methods  
✅ Monitor payment status  
✅ Payment history reports  

### User Management
✅ Create and manage users  
✅ Assign roles (4 role types)  
✅ Role-based access control  
✅ Profile management  

### Analytics & Reporting
✅ Dashboard with statistics  
✅ Order analytics  
✅ Supplier analysis  
✅ Payment summaries  

### System Management
✅ Settings configuration  
✅ System backup  
✅ Feedback collection  
✅ User feedback system  

---

## 👥 Demo Accounts

| Role | Username | Password |
|------|----------|----------|
| **Administrator** | dennis | lopez |
| **Purchasing Officer** | jani | jani |
| **Finance Officer** | angel | angel |
| **Store Owner** | jennifer | jennifer |

---

## 🔧 Technology Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Runtime |
| **Flask** | 2.3.2 | Web framework |
| **MongoDB** | 4.0+ | Database |
| **PyMongo** | 4.4.1 | MongoDB driver |
| **Werkzeug** | 2.3.6 | WSGI utilities |

---

## 📋 Pre-Requisites

- **Python 3.8** or higher
- **MongoDB 4.0+** (local or MongoDB Atlas cloud)
- **pip** (Python package manager)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

---

## 🚀 Deployment Steps

### 1. Install MongoDB

**Local Installation:**
- Windows: Download from [mongodb.com](https://www.mongodb.com/try/download/community)
- macOS: `brew install mongodb-community`
- Linux: `sudo apt-get install mongodb`

**Cloud Option:**
- MongoDB Atlas: [atlas.mongodb.com](https://www.mongodb.com/cloud/atlas) (free tier available)

### 2. Configure Environment

```bash
# Copy template to runtime config
cp .env.example .env

# Edit .env with MongoDB connection string
# For local: MONGODB_URI=mongodb://localhost:27017
# For Atlas: MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python app.py
```

Application runs on: **http://127.0.0.1:5000**

### 5. Login & Test

Open browser and login with demo credentials:
- Username: **dennis**
- Password: **lopez**

---

## 🔄 Upgrading from v1.0 (JSON Edition)

If you have existing JSON data:

```bash
# Automatic backup and migration
python migrate_json_to_mongodb.py
```

The script will:
1. Create backup in `data_backup_YYYYMMDD_HHMMSS/`
2. Transfer all data to MongoDB
3. Report migration summary

See **[CHANGELOG.md](CHANGELOG.md)** for detailed changes.

---

## 🧪 Testing & Verification

Complete testing guide: **[TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)**

Test categories include:
- Environment setup verification
- Application startup
- Database initialization
- Authentication
- All module operations
- API endpoints
- Error handling
- Performance

---

## 📊 Database Collections

Auto-created and initialized:

| Collection | Purpose |
|-----------|---------|
| **users** | User accounts (4 demo users) |
| **suppliers** | Supplier information |
| **orders** | Purchase orders |
| **payments** | Payment records |
| **feedback** | User feedback |
| **settings** | System configuration |

---

## 🔐 Security

### Implemented
✅ SHA256 password hashing  
✅ Session-based authentication  
✅ Role-based access control  
✅ Unique constraints on critical fields  
✅ Secure file upload handling  

### Recommended for Production
📌 Change SECRET_KEY to random value  
📌 Enable SESSION_COOKIE_SECURE for HTTPS  
📌 Use MongoDB Atlas for cloud deployment  
📌 Implement rate limiting  
📌 Enable MongoDB authentication  
📌 Set up regular backups  

---

## ✅ Project Status

| Aspect | Status |
|--------|--------|
| Code | ✅ Complete & tested |
| Features | ✅ All functional |
| Documentation | ✅ Comprehensive |
| Testing | ✅ 20+ test scenarios |
| Deployment | ✅ Ready for production |

---

## 🚀 Get Started Now

### For Quick Start (5 minutes)
👉 **[Read QUICKSTART.md](QUICKSTART.md)**

### For Complete Setup
👉 **[Read SETUP_GUIDE.md](SETUP_GUIDE.md)**

### To Find Specific Help
👉 **[Read INDEX.md](INDEX.md)** - Documentation roadmap

### To Understand the System
👉 **[Read README_MONGODB.md](README_MONGODB.md)**

---

## 📞 Support

- **Setup Issues?** → See [SETUP_GUIDE.md#troubleshooting](SETUP_GUIDE.md)
- **Testing Help?** → See [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)
- **Technical Questions?** → See [README_MONGODB.md](README_MONGODB.md)
- **Migration Issues?** → See [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md)
- **Need Overview?** → See [INDEX.md](INDEX.md)

---

## 📄 License

[Add your license information here]

---

**Version**: 2.0 (MongoDB Edition)  
**Status**: Production Ready ✅  
**Ready to get started?** → [Read QUICKSTART.md](QUICKSTART.md)

## Accounts

- **Admin** - Username: dennis, Password: lopez
- **Purchasing Officer** - Username: jani, Pasword: jani
- **Finance Officer** - Username: angel, Password: angel
- **Store owner** - Username: jennifer, Password: jennifer

## Project Modules

### Module 1: Supplier Management

This module is implemented and functional in the current code.

**Features:**
- Add new supplier
- View supplier list
- Update supplier information
- Delete supplier
- Search suppliers by text and status
- Display supplier details in the supplier list

**How it works:**
- The `suppliers` route loads supplier data from `data/suppliers.json`.
- `templates/suppliers.html` provides a searchable table and modal form for add/edit.
- The API endpoints `/api/suppliers` and `/api/suppliers/<sid>` handle create, update, and delete actions.

### Module 2: Purchase Order Management

This module is implemented and functional in the current code.

**Features:**
- Create new purchase order
- Select supplier from existing suppliers
- Add product/item and quantity
- Enter unit price
- Automatically compute subtotal and total
- Update order details/status
- Cancel purchase order via status field
- Track order status as Pending, Approved, Delivered, or Cancelled

**How it works:**
- The `orders` route loads data from `data/orders.json` and supplier names from `data/suppliers.json`.
- `templates/purchase_orders.html` provides a creation modal, order table, search, and status update interface.
- The API endpoints `/api/orders` and `/api/orders/<po_number>` handle order creation and updating.

### Module 3: Delivery and Receiving

This module is partially implemented through order status management.

**Implemented behavior:**
- Delivered items are tracked by the order `status` field.
- The `delivery` field records the expected or actual delivery date.
- Order completion is verified by setting status to `Delivered`.
- Delivery status can be updated through the order status edit workflow.

**Note:**
- There is no separate dedicated delivery-only route or receiving form in the current code.
- Delivery handling is currently integrated into purchase order status updates.

### Module 4: Payment Method Management

This module is implemented and functional in the current code.

**Features:**
- Record supplier payment
- Select payment method (`Bank Transfer`, `Check`, `Cash`)
- Update payment status (`Pending`, `Partial`, `Paid`)
- View payment history and status in a searchable table

**How it works:**
- The `payments` route loads data from `data/payments.json` and existing purchase orders from `data/orders.json`.
- `templates/payments.html` provides a payment-record modal, order selection, auto-fill supplier/total amount, and status editing.
- The API endpoints `/api/payments` and `/api/payments/<payment_id>` handle payment create and status updates.

### Module 5: Reporting

This module is implemented and functional in the current code.

**Features:**
- Purchase order reporting
- Displays orders grouped by status
- Summarizes totals for pending, delivered, and approved orders
- Excludes cancelled orders from the main purchase order report table

**How it works:**
- The `reports` route loads orders, payments, suppliers, and feedback data.
- `templates/reports.html` renders a report table and summary metrics derived from current order data.

## Usage

1. Run the app:

   ```powershell
   python app.py
   ```

2. Open this URL in your browser:

   ```text
   http://127.0.0.1:5000
   ```

3. Login with demo credentials or add new users manually in `data/users.json`.

4. Use the navigation menu to access:
   - Suppliers
   - Purchase Orders
   - Payments
   - Reports

## Notes

- Data is stored in JSON files under `data/`.
- The current code does not include a dedicated product/item master module; product details are entered directly on purchase orders.
- Delivery and receiving are managed through order status updates rather than a separate delivery workflow.

Currently developing the live web.
