# SPOMS MongoDB Migration - Testing Checklist

## Pre-Deployment Verification

### 1. Environment Setup
- [ ] Python 3.8+ installed
- [ ] MongoDB running (local or Atlas configured)
- [ ] `.env` file created with valid MONGODB_URI
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] All required packages visible in: `pip list`

### 2. Application Startup
- [ ] Run `python app.py` without errors
- [ ] No connection errors displayed
- [ ] Application running on http://127.0.0.1:5000
- [ ] No Python syntax errors
- [ ] MongoDB auto-initialization completed successfully

### 3. Database Initialization
- [ ] Collections created automatically (users, suppliers, orders, payments, feedback, settings)
- [ ] Default user accounts initialized
- [ ] Indexes created (unique on username, supplier id, order po, etc.)
- [ ] No duplicate index errors

### 4. Authentication
- [ ] Login page loads at http://127.0.0.1:5000/login
- [ ] Can login with demo account: dennis/lopez
- [ ] Can login with demo account: jani/jani
- [ ] Can login with demo account: angel/angel
- [ ] Can login with demo account: jennifer/jennifer
- [ ] Session creates properly
- [ ] Invalid password rejected
- [ ] Non-existent user rejected

### 5. Dashboard
- [ ] Dashboard loads after login
- [ ] Statistics display correctly:
  - [ ] Total Suppliers count
  - [ ] Total Orders count
  - [ ] Total Payments count
  - [ ] Total Users count
- [ ] Recent activity visible
- [ ] Charts render properly

### 6. Suppliers Module
- [ ] Suppliers page loads
- [ ] Can view all suppliers
- [ ] Can add new supplier
- [ ] Can edit existing supplier
- [ ] Can delete supplier
- [ ] Duplicate supplier ID prevented
- [ ] Supplier data persists in MongoDB

### 7. Orders Module
- [ ] Orders page loads
- [ ] Can view all orders
- [ ] Can add new order
- [ ] Can update order status
- [ ] Can delete order
- [ ] Order PO number unique constraint works
- [ ] Order data persists in MongoDB

### 8. Payments Module
- [ ] Payments page loads
- [ ] Can view all payments
- [ ] Can add new payment
- [ ] Can update payment status
- [ ] Can delete payment
- [ ] Payment data persists in MongoDB

### 9. Users Module
- [ ] Users page loads
- [ ] Can view all users
- [ ] Can add new user
- [ ] Can edit user
- [ ] Can delete user
- [ ] Duplicate username prevented
- [ ] Password hashing works
- [ ] User passwords not exposed in API responses

### 10. Feedback Module
- [ ] Feedback page loads
- [ ] Can submit feedback
- [ ] Can view all feedback
- [ ] Feedback data persists with timestamps
- [ ] Feedback data visible in MongoDB

### 11. Settings Module
- [ ] Settings page loads
- [ ] Can update system settings
- [ ] Settings changes persist
- [ ] Logo upload works
- [ ] Background image upload works

### 12. Reports & Analytics
- [ ] Reports page loads
- [ ] Statistics calculated correctly:
  - [ ] Order status distribution
  - [ ] Supplier statistics
  - [ ] Payment summaries
- [ ] Charts render properly
- [ ] Data aggregation working from MongoDB

### 13. User Profile
- [ ] Profile page loads
- [ ] Can view profile information
- [ ] Can update profile
- [ ] Can change password
- [ ] Can upload profile picture
- [ ] Changes persist

### 14. API Endpoints
- [ ] `GET /api/suppliers` returns JSON array
- [ ] `POST /api/suppliers` creates new supplier
- [ ] `PUT /api/suppliers/<id>` updates supplier
- [ ] `DELETE /api/suppliers/<id>` deletes supplier
- [ ] `GET /api/orders` returns orders
- [ ] `POST /api/orders` creates order
- [ ] `PUT /api/orders/<po>` updates order
- [ ] `GET /api/payments` returns payments
- [ ] `POST /api/payments` creates payment
- [ ] `PUT /api/payments/<id>` updates payment
- [ ] `GET /api/users` returns users (no passwords)
- [ ] `POST /api/users` creates user
- [ ] `PUT /api/users/<id>` updates user
- [ ] `DELETE /api/users/<id>` deletes user

### 15. Error Handling
- [ ] Invalid URLs return 404 page
- [ ] Unauthorized access returns 403 page
- [ ] Application errors return 500 page gracefully
- [ ] MongoDB connection errors handled properly
- [ ] Duplicate key errors handled gracefully

### 16. Data Migration (If Applicable)
- [ ] Backup created successfully
- [ ] `python migrate_json_to_mongodb.py` completes without errors
- [ ] All data migrated from JSON files to MongoDB
- [ ] Migrated data accessible in application
- [ ] No data loss detected

### 17. Session Management
- [ ] Session timeout works (1 hour default)
- [ ] Logout clears session
- [ ] Multiple users can be logged in
- [ ] Session security (HttpOnly cookies if HTTPS)

### 18. File Uploads
- [ ] Profile picture upload works
- [ ] File saved to static/images
- [ ] Invalid file types rejected
- [ ] Large files handled appropriately

### 19. Role-Based Access
- [ ] Administrator can access all features
- [ ] Purchasing Officer restrictions work
- [ ] Finance Officer restrictions work
- [ ] Store Owner restrictions work
- [ ] Unauthorized role access denied

### 20. MongoDB Collections Verification
Run these MongoDB commands to verify:

```javascript
// Connect to MongoDB
use spoms

// Verify collections exist
show collections

// Verify data in users collection
db.users.find().pretty()

// Verify indexes
db.users.getIndexes()

// Verify count
db.suppliers.countDocuments()
db.orders.countDocuments()
db.payments.countDocuments()
```

## Performance Testing

- [ ] Application loads in < 2 seconds
- [ ] Database queries complete within 500ms
- [ ] No memory leaks after 30 minutes of use
- [ ] Can handle 10+ simultaneous API requests

## Final Sign-Off

- [ ] All checklist items verified
- [ ] No critical bugs found
- [ ] Application ready for production
- [ ] Documentation reviewed
- [ ] Backup and recovery process tested

---

**Test Date**: _______________
**Tester Name**: _______________
**Sign-Off**: _______________
