# ⚡ SPOMS Vercel Environment Variables - Quick Reference

## 🎯 The 4 Required Variables

### For Vercel Dashboard → Settings → Environment Variables

```
┌─────────────────────────────────────────────────────────────────────┐
│ Variable 1: MONGODB_URI                                             │
├─────────────────────────────────────────────────────────────────────┤
│ Value: mongodb+srv://username:password@cluster.mongodb.net/spoms... │
│ Purpose: Connect to MongoDB database                                 │
│ Status: ✅ REQUIRED                                                  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ Variable 2: MONGODB_DB_NAME                                         │
├─────────────────────────────────────────────────────────────────────┤
│ Value: spoms                                                         │
│ Purpose: Database name                                               │
│ Status: ✅ REQUIRED                                                  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ Variable 3: FLASK_ENV                                               │
├─────────────────────────────────────────────────────────────────────┤
│ Value: production                                                    │
│ Purpose: Enable production mode                                      │
│ Status: ✅ REQUIRED                                                  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ Variable 4: SECRET_KEY                                              │
├─────────────────────────────────────────────────────────────────────┤
│ Value: [Your 64-character random string]                            │
│ Purpose: Encrypt user sessions                                       │
│ Status: ✅ REQUIRED                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Where to Get Each Value

### 1. MONGODB_URI
**From**: MongoDB Atlas Dashboard
**Steps**:
1. Login to MongoDB Atlas: https://cloud.mongodb.com
2. Click "Connect" on your cluster
3. Choose "Drivers"
4. Copy connection string
5. Replace `<username>` and `<password>`
6. Paste in Vercel

**Example Format**:
```
mongodb+srv://spoms_user:MyPassword123@cluster0.xxxxx.mongodb.net/spoms?retryWrites=true&w=majority
```

### 2. MONGODB_DB_NAME
**Value**: Always `spoms`
**No setup needed** - just copy/paste

### 3. FLASK_ENV
**Value**: Always `production`
**No setup needed** - just copy/paste

### 4. SECRET_KEY
**Generate with**:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
**Example Output**:
```
f1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e
```
**Copy the output** and paste in Vercel

---

## 📝 Vercel Setup Steps (5 minutes)

```
1. Go to: https://vercel.com/dashboard
2. Click on SPOMS project
3. Click: Settings → Environment Variables
4. Click: Add New
   Name: MONGODB_URI
   Value: [Your MongoDB connection string]
   Click: Add
5. Click: Add New
   Name: MONGODB_DB_NAME
   Value: spoms
   Click: Add
6. Click: Add New
   Name: FLASK_ENV
   Value: production
   Click: Add
7. Click: Add New
   Name: SECRET_KEY
   Value: [Your generated SECRET_KEY]
   Click: Add
8. Scroll to Deployments
9. Find latest deployment
10. Click: Redeploy
11. Wait 2-3 minutes
12. Test your app
```

---

## ✅ Verification

### Check if Variables Are Working

**Method 1: Check App**
- Open your Vercel URL
- Try login: `dennis` / `lopez`
- If it works → Variables are correct ✅

**Method 2: Check Logs**
- Go to Deployments
- Click latest deployment
- Click Logs
- Look for: `✓ Connected to MongoDB successfully`

**Method 3: Check Console Output**
- Should see: `✓ MongoDB connected`
- Should NOT see: `✗ MongoDB connection failed`

---

## 🆘 If Something Goes Wrong

| Problem | Check This |
|---------|-----------|
| "MongoDB not connected" | Is MONGODB_URI correct? |
| "Auth failed" | Is username/password correct? |
| "Network error" | Is IP whitelisted in MongoDB Atlas? |
| "Secret key error" | Is SECRET_KEY 64+ characters? |
| "App won't start" | Check Vercel Logs tab |

---

## 📊 Variable Summary Table

| Name | Value | Where From | Used For |
|------|-------|-----------|----------|
| MONGODB_URI | `mongodb+srv://...` | MongoDB Atlas | Database connection |
| MONGODB_DB_NAME | `spoms` | Fixed value | Database name |
| FLASK_ENV | `production` | Fixed value | Production mode |
| SECRET_KEY | Random string | Generate | Session encryption |

---

## 🎓 Understanding Each Variable

### MONGODB_URI (Most Important!)
This is how your app talks to the database. Without it, nothing works.
- **Format**: `mongodb+srv://username:password@host/database?options`
- **Changes**: Different for every user
- **Security**: Keep it secret!

### MONGODB_DB_NAME
Tells the app which database to use.
- **Value**: Always `spoms` for this project
- **Changes**: Never (unless you rename database)
- **Security**: Not sensitive

### FLASK_ENV
Determines if app runs in development or production mode.
- **Value**: `production` for Vercel, `development` for local
- **Changes**: Different per environment
- **Security**: Not sensitive, but important for performance

### SECRET_KEY
Encrypts user session data (login info, etc).
- **Format**: Random 64+ character string
- **Changes**: Generate new for production
- **Security**: VERY SENSITIVE - keep secret!

---

## 🚀 Quick Copy-Paste Template

When adding variables in Vercel, use this format:

```
Name: MONGODB_URI
Value: mongodb+srv://YOUR_USER:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/spoms?retryWrites=true&w=majority

Name: MONGODB_DB_NAME
Value: spoms

Name: FLASK_ENV
Value: production

Name: SECRET_KEY
Value: [YOUR_GENERATED_64_CHAR_STRING]
```

---

## ⚠️ Critical Security Notes

```
🔒 DO THIS:
✓ Use strong MongoDB password (12+ chars, mix of everything)
✓ Generate unique SECRET_KEY for production
✓ Store credentials only in Vercel env vars
✓ Delete this reference file after deployment
✓ Rotate credentials monthly in production

🚫 NEVER DO THIS:
✗ Put credentials in code files
✗ Commit .env to GitHub
✗ Share your credentials
✗ Use same key for dev and production
✗ Whitelist 0.0.0.0/0 permanently
```

---

**All set! Your SPOMS app needs exactly 4 environment variables. Set them in Vercel and you're good to go!** 🚀
