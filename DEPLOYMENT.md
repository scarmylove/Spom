# SPOMS Vercel Deployment Guide

## ✅ Deployment Checklist

- [x] Added `vercel.json` configuration
- [x] Added `.vercelignore` for optimized builds
- [x] Updated `requirements.txt` with gunicorn
- [x] Updated `app.py` for production mode
- [x] Enhanced `.env.example` with Vercel setup instructions

---

## 🚀 Step-by-Step Deployment

### Step 1: Prepare MongoDB Atlas (Cloud Database)

Since Vercel is serverless and cannot connect to local MongoDB, you **MUST** use MongoDB Atlas.

1. **Create MongoDB Atlas Account**
   - Go to https://www.mongodb.com/cloud/atlas
   - Sign up (free tier available)

2. **Create a Cluster**
   - Click "Create a Deployment"
   - Select "M0 Sandbox" (free tier)
   - Choose region closest to your app
   - Create cluster (takes 2-3 minutes)

3. **Create Database User**
   - Go to "Database Access"
   - Click "Add Database User"
   - Username: `spoms_user` (or any username)
   - Password: Create strong password (save it!)
   - Built-in Role: "Atlas Admin"
   - Click "Add User"

4. **Allow Vercel Access**
   - Go to "Network Access"
   - Click "Add IP Address"
   - Select "Allow access from anywhere" (0.0.0.0/0)
   - Click "Confirm"
   - ⚠️ Note: For production, restrict to Vercel IPs

5. **Get Connection String**
   - Click "Databases" → "Connect"
   - Choose "Drivers"
   - Select "Node.js" driver (the format is the same)
   - Copy connection string that looks like:
     ```
     mongodb+srv://spoms_user:password@cluster0.xxxxx.mongodb.net/spoms?retryWrites=true&w=majority
     ```
   - Replace `<password>` with actual password
   - Change database name to `spoms`

---

### Step 2: Prepare Your GitHub Repository

1. **Initialize Git (if not already)**
   ```bash
   git init
   git add .
   git commit -m "Prepare for Vercel deployment"
   ```

2. **Push to GitHub**
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/SPOMS-Vercel.git
   git push -u origin main
   ```

---

### Step 3: Connect to Vercel

1. **Go to Vercel**
   - Visit https://vercel.com
   - Click "Sign Up" (use GitHub account)
   - Authorize Vercel to access your GitHub

2. **Import Project**
   - Click "New Project"
   - Select "Import Git Repository"
   - Choose `SPOMS-Vercel` repository
   - Click "Import"

3. **Configure Project**
   - **Project Name**: `spoms` (or your choice)
   - **Framework**: Python
   - **Root Directory**: `.` (current)

4. **Add Environment Variables**
   
   Click "Environment Variables" and add:
   
   | Variable | Value |
   |----------|-------|
   | MONGODB_URI | `mongodb+srv://spoms_user:PASSWORD@cluster.mongodb.net/spoms?retryWrites=true&w=majority` |
   | MONGODB_DB_NAME | `spoms` |
   | FLASK_ENV | `production` |
   | SECRET_KEY | Generate with: `python -c "import secrets; print(secrets.token_hex(32))"` |

5. **Deploy**
   - Click "Deploy"
   - Wait for build to complete (2-3 minutes)
   - Get your live URL: `https://spoms.vercel.app`

---

### Step 4: Test Deployment

1. **Check Build Logs**
   - In Vercel Dashboard: "Deployments" → Latest
   - Look for success message or errors

2. **Test Your App**
   - Open your Vercel URL
   - Try logging in with demo credentials:
     - Username: `dennis`
     - Password: `lopez`

3. **Verify MongoDB Connection**
   - If login works, MongoDB is connected ✅
   - If login fails, check deployment logs for MongoDB errors

---

## 🔧 Environment Variables Reference

Add these in Vercel Dashboard → Settings → Environment Variables:

```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/spoms?retryWrites=true&w=majority
MONGODB_DB_NAME=spoms
FLASK_ENV=production
SECRET_KEY=your-secure-random-string-here
```

---

## 📝 Configuration Files Created

### vercel.json
- Tells Vercel how to build and run your Python app
- Routes all requests to Flask app
- Sets environment variables

### .vercelignore
- Excludes unnecessary files from deployment
- Reduces deployment size
- Speeds up builds

### requirements.txt (Updated)
- Added `gunicorn==21.2.0` for production WSGI server

### app.py (Updated)
- Production mode detection
- Disables debug in production

### .env.example (Enhanced)
- Clear MongoDB Atlas setup instructions
- Vercel deployment steps
- Security notes

---

## ⚠️ Important Notes

### Security
- Never commit `.env` file (it's in `.gitignore`)
- Use strong MongoDB passwords
- Change `SECRET_KEY` for production
- In production, restrict MongoDB IP whitelist to Vercel only

### Common Issues

**Issue**: "MongoDB connection failed"
- ✅ Solution: Verify MongoDB Atlas connection string
- ✅ Solution: Check if IP is whitelisted
- ✅ Solution: Verify username/password are correct

**Issue**: "Import Error: No module named 'pymongo'"
- ✅ Solution: This shouldn't happen (Vercel auto-installs from requirements.txt)
- ✅ Solution: Check if requirements.txt was updated

**Issue**: "Application Error: Server Error"
- ✅ Check Vercel logs for detailed error
- ✅ Verify all environment variables are set
- ✅ Verify MongoDB connection works

---

## 🔄 Deployment Workflow

1. **Local Development**
   ```bash
   # Local MongoDB or MongoDB Atlas
   python app.py
   ```

2. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Your message"
   git push
   ```

3. **Automatic Deployment**
   - Vercel auto-deploys on push to main branch
   - Check deployment status in Vercel Dashboard
   - Live URL updates automatically

4. **Rollback if Needed**
   - In Vercel Dashboard, click previous deployment
   - Click "Redeploy"

---

## 📊 Monitoring

### Vercel Dashboard
- **Deployments**: See all versions deployed
- **Logs**: View real-time and historical logs
- **Usage**: Check function invocations
- **Settings**: Manage environment variables

### MongoDB Atlas
- **Metrics**: Database performance and usage
- **Activity**: User and cluster activity logs
- **Alerts**: Set up alerts for high usage

---

## 🎯 Next Steps

1. ✅ Set up MongoDB Atlas cluster
2. ✅ Configure environment variables in Vercel
3. ✅ Deploy and test
4. ✅ Set custom domain (optional)
5. ✅ Monitor logs and performance
6. ✅ Set up alerts

---

## 📚 Reference Links

- **Vercel Python Docs**: https://vercel.com/docs/concepts/functions/serverless-functions/python
- **MongoDB Atlas**: https://www.mongodb.com/cloud/atlas
- **Flask Deployment**: https://flask.palletsprojects.com/deployment/
- **Gunicorn**: https://gunicorn.org/

---

## 💡 Pro Tips

1. **Use MongoDB Atlas Free Tier** - Perfect for learning and testing
2. **Monitor Spending** - Set up billing alerts on Vercel
3. **Keep Secrets Safe** - Never commit `.env` or credentials
4. **Test Thoroughly** - Test in staging before production
5. **Enable HTTPS** - Vercel provides free HTTPS by default

---

## ✨ You're Ready to Deploy!

Your SPOMS application is now configured for Vercel. Follow the steps above and you'll have a live application in minutes!

Need help? Check the logs in Vercel Dashboard → Deployments → Your Latest Deployment → Logs
