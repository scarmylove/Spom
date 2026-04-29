# Vercel Deployment Quick Commands

## 1️⃣ MongoDB Atlas Setup (3 minutes)

```bash
# Visit MongoDB Atlas
https://www.mongodb.com/cloud/atlas

# Create cluster, then copy connection string:
# Format: mongodb+srv://username:password@cluster.mongodb.net/spoms
```

## 2️⃣ Git Commands

```bash
# Initialize Git
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Commit
git commit -m "Ready for Vercel deployment"

# Create main branch and push
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/SPOMS-Vercel.git
git push -u origin main
```

## 3️⃣ Vercel Deployment

```bash
# Visit Vercel
https://vercel.com

# Steps:
# 1. Sign up with GitHub
# 2. Click "New Project"
# 3. Import "SPOMS-Vercel" repository
# 4. Add Environment Variables:
#    MONGODB_URI: (from MongoDB Atlas)
#    MONGODB_DB_NAME: spoms
#    FLASK_ENV: production
#    SECRET_KEY: (generate: python -c "import secrets; print(secrets.token_hex(32))")
# 5. Click Deploy
# 6. Wait 2-3 minutes
# 7. Get live URL
```

## 4️⃣ Generate SECRET_KEY

```bash
python -c "import secrets; print(secrets.token_hex(32))"

# Output will be 64-character random string
# Copy and paste into Vercel environment variables
```

## 5️⃣ Test Deployment

```bash
# Open in browser:
https://your-app-name.vercel.app

# Login with:
# Username: dennis
# Password: lopez

# Check if all features work:
# - Dashboard loads
# - Can view suppliers
# - Can create orders
# - Can record payments
```

## 6️⃣ Check Logs (if deployment fails)

```bash
# In Vercel Dashboard:
# Click on your project
# Click "Deployments"
# Click latest deployment
# Click "Logs" tab
# Look for error messages related to MongoDB or Python
```

## 📋 Environment Variables to Add in Vercel

```
MONGODB_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/spoms?retryWrites=true&w=majority
MONGODB_DB_NAME=spoms
FLASK_ENV=production
SECRET_KEY=your-64-character-random-string-here
```

## 🔗 Important Links

- **Vercel**: https://vercel.com
- **MongoDB Atlas**: https://www.mongodb.com/cloud/atlas
- **GitHub**: https://github.com
- **Your Deployed App**: https://your-app-name.vercel.app

## ⚡ Quick Status Check

```bash
# After deployment, these should work:
# ✅ App loads at Vercel URL
# ✅ Login page appears
# ✅ Demo login works (dennis/lopez)
# ✅ Dashboard loads with statistics
# ✅ MongoDB connection successful
```

## 🆘 Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| MongoDB Connection Error | Check MONGODB_URI in Vercel env vars |
| 404 Page Not Found | Clear browser cache, refresh |
| Login Failed | Verify MongoDB user created in Atlas |
| Slow Loading | Check internet connection, MongoDB IP whitelist |
| Deployment Fails | Check Vercel logs, verify requirements.txt |

## 💡 Pro Tips

1. **Keep .env local** - Never commit to GitHub
2. **Test locally first** - Run `python app.py` before deploying
3. **Monitor logs** - Check Vercel logs for issues
4. **Use strong passwords** - For MongoDB user
5. **Set custom domain** - In Vercel settings (optional)

## 📞 Troubleshooting Commands

```bash
# Test MongoDB connection locally first
python test.py

# Check if requirements.txt is correct
pip install -r requirements.txt

# Verify Flask runs locally
python app.py

# Check Python version
python --version  # Should be 3.8+
```

---

**Status**: Your SPOMS app is ready for Vercel deployment! 🚀
