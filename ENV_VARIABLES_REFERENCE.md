# SPOMS Environment Variables for Vercel Deployment

## 🔑 Required Environment Variables

These MUST be set in Vercel Dashboard for the app to work:

### 1. **MONGODB_URI** (Required - Critical)
**Purpose**: MongoDB connection string  
**Format**: `mongodb+srv://username:password@cluster.mongodb.net/spoms?retryWrites=true&w=majority`

**Example**:
```
mongodb+srv://spoms_user:MyStrongPassword123@cluster0.xxxxx.mongodb.net/spoms?retryWrites=true&w=majority
```

**How to Get**:
1. Go to MongoDB Atlas Dashboard
2. Click "Connect" → "Drivers"
3. Copy the connection string
4. Replace `<username>` with your database user
5. Replace `<password>` with your database password
6. Replace database name with `spoms`

**⚠️ SECURITY**: Never commit this to GitHub! Use Vercel Environment Variables only.

---

### 2. **MONGODB_DB_NAME** (Required)
**Purpose**: MongoDB database name  
**Value**: `spoms`

**Why**: Tells the app which database to use

---

### 3. **FLASK_ENV** (Required)
**Purpose**: Flask environment mode  
**Value for Vercel**: `production`

**What it does**:
- Disables Flask debug mode
- Enables secure cookies (HTTPS only)
- Optimizes performance
- Sets strict CORS policies

---

### 4. **SECRET_KEY** (Required - Critical)
**Purpose**: Flask session encryption key  
**Format**: 32+ character random string

**Generate a Secure KEY**:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Example Output**:
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

**Why**: Protects user sessions from tampering

**⚠️ SECURITY**: 
- Generate a NEW key for production
- Never reuse your development key
- Keep it secret

---

## 📋 Complete Environment Variables Table

| Variable | Required | Default | Type | Example |
|----------|----------|---------|------|---------|
| MONGODB_URI | ✅ YES | None | String | `mongodb+srv://user:pass@cluster.mongodb.net/spoms?...` |
| MONGODB_DB_NAME | ✅ YES | spoms | String | `spoms` |
| FLASK_ENV | ✅ YES | development | String | `production` |
| SECRET_KEY | ✅ YES | None | String | `a1b2c3d4e5f6...` |

---

## 🔧 How to Set Environment Variables in Vercel

### Method 1: Vercel Dashboard (Recommended)

1. Go to **https://vercel.com/dashboard**
2. Select your **SPOMS** project
3. Click **Settings**
4. Click **Environment Variables** (left sidebar)
5. Add each variable:
   - **Name**: MONGODB_URI
   - **Value**: `mongodb+srv://...`
   - Click **Add**
6. Repeat for: MONGODB_DB_NAME, FLASK_ENV, SECRET_KEY
7. Click **Save**
8. **Redeploy** to apply changes

---

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Link your project
vercel

# Add environment variables
vercel env add MONGODB_URI
vercel env add MONGODB_DB_NAME
vercel env add FLASK_ENV
vercel env add SECRET_KEY

# Re-deploy with new variables
vercel --prod
```

---

## ✅ Pre-Deployment Checklist

Before deploying to Vercel, verify you have:

- [ ] MongoDB Atlas account created
- [ ] M0 free cluster created
- [ ] Database user created with strong password
- [ ] IP whitelist configured (0.0.0.0/0 or Vercel IPs)
- [ ] Connection string copied
- [ ] SECRET_KEY generated
- [ ] All 4 environment variables in Vercel Dashboard
- [ ] GitHub repository pushed with latest code
- [ ] vercel.json configured
- [ ] requirements.txt includes gunicorn

---

## 🔒 Security Best Practices

### ✅ DO:
```
✓ Use strong MongoDB passwords (12+ characters, mixed case, numbers, symbols)
✓ Generate unique SECRET_KEY for production
✓ Store all secrets in Vercel Environment Variables
✓ Rotate credentials periodically
✓ Use MongoDB Atlas IP whitelist for production
✓ Monitor MongoDB access logs
```

### ❌ DON'T:
```
✗ Don't commit .env file to GitHub
✗ Don't hardcode credentials in vercel.json
✗ Don't reuse development credentials in production
✗ Don't whitelist 0.0.0.0/0 permanently in production
✗ Don't share SECRET_KEY or MongoDB password
✗ Don't use weak passwords
```

---

## 🧪 Verify Environment Variables Are Set

After deploying, verify variables are working:

### Check Vercel Logs
1. Go to Vercel Dashboard
2. Select your project
3. Click **Deployments**
4. Click latest deployment
5. Click **Logs**
6. Look for: `✓ Connected to MongoDB successfully`

### Test Live App
```
1. Open your Vercel URL
2. Try login with: dennis / lopez
3. If successful → All variables configured correctly ✅
4. If failed → Check Vercel logs for errors
```

---

## 🆘 Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "MongoDB connection failed" | Wrong MONGODB_URI | Verify connection string in MongoDB Atlas |
| "Authentication failed" | Wrong username/password | Check MongoDB user credentials |
| "Network error" | IP not whitelisted | Whitelist 0.0.0.0/0 in MongoDB Atlas |
| "Invalid SECRET_KEY" | Empty or missing | Generate new SECRET_KEY and set in Vercel |
| "App crashes on startup" | Missing environment variable | Verify all 4 variables in Vercel Dashboard |

---

## 📊 Environment Variables by Environment

### Development (Local Machine)
```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=spoms
FLASK_ENV=development
SECRET_KEY=dev-key-no-need-to-be-secure
```

### Production (Vercel)
```env
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/spoms?retryWrites=true&w=majority
MONGODB_DB_NAME=spoms
FLASK_ENV=production
SECRET_KEY=secure-random-64-character-string
```

---

## 🔗 Related Resources

- **MongoDB Atlas Setup**: https://docs.mongodb.com/atlas/setup-atlas-account/
- **Vercel Environment Variables**: https://vercel.com/docs/concepts/projects/environment-variables
- **Flask Configuration**: https://flask.palletsprojects.com/config/
- **Security Best Practices**: https://owasp.org/

---

## ⚡ Quick Setup Summary

```bash
# 1. Generate SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"

# 2. Set in Vercel (copy the output above)
# → Go to Vercel Dashboard → Settings → Environment Variables

# 3. Add these variables:
# MONGODB_URI: mongodb+srv://user:password@cluster.mongodb.net/spoms?...
# MONGODB_DB_NAME: spoms
# FLASK_ENV: production
# SECRET_KEY: (your generated key)

# 4. Redeploy
# → Click "Redeploy" on latest deployment

# 5. Test
# → Open your Vercel URL and login with dennis/lopez
```

---

**Status**: Your SPOMS app requires 4 environment variables for Vercel deployment. All are critical! ✅
