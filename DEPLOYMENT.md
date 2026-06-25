# Railway Deployment Guide for F1 Encyclopedia

## Super Easy 5-Minute Deployment

### Step 1: Go to Railway.app (1 minute)
- Visit https://railway.app
- Click "Sign up"
- Select "Continue with GitHub"
- Authorize Railway to access your GitHub

### Step 2: Create Project (2 minutes)
- Click "Create new project"
- Select "Deploy from GitHub repo"
- Find and select your `f1-ency` repository
- Railway will auto-detect it's Django

### Step 3: Add PostgreSQL Database (1 minute)
- In your Railway project, click "Add"
- Search for "Postgres"
- Click it to add (Railway auto-creates DATABASE_URL)

### Step 4: Set Environment Variables (1 minute)
- Click "Variables" in Railway
- Add these:
  ```
  SECRET_KEY=django-insecure-your-random-secret-key-123456789
  DEBUG=False
  ALLOWED_HOSTS=*.railway.app
  ```

### Step 5: Deploy! (automatic)
- Railway automatically deploys from your GitHub
- Wait ~2-3 minutes
- Your URL appears in the deployment panel
- **Share that URL with anyone!** 🎉

## That's it! Your site is live online!

### Troubleshooting:
- If deployment fails, check Railway's logs
- Make sure all files are pushed to GitHub (git status)
- Verify environment variables are set
