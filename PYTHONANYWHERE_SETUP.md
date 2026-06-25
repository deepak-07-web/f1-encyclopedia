# PYTHONANYWHERE DEPLOYMENT GUIDE

## Quick Setup (5 minutes)

### 1. Open Bash Console
- PythonAnywhere Dashboard → **New console** → **Bash**

### 2. Clone Your Repository
```bash
cd ~
git clone https://github.com/deepak-07-web/f1-encyclopedia.git
cd f1-encyclopedia
```

### 3. Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.9 f1_env
pip install -r requirements.txt
```

### 4. Setup Database
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py add_comprehensive_data
```

### 5. Create Web App
1. Go to **"All web apps"** tab in PythonAnywhere
2. Click **"Add a new web app"**
3. Choose your domain: `yourname.pythonanywhere.com` (FREE)
4. Select **Django** framework
5. Choose **Python 3.9**
6. Click create

### 6. Configure WSGI
1. In **"All web apps"**, click your new web app name
2. Under **Code** section, click **"WSGI configuration file"**
3. Replace everything with the content from `pythonanywhere_wsgi.py`
4. Change `{username}` to your PythonAnywhere username
5. Save and reload the web app

### 7. Set Static Files
Still in web app settings:
- **Static files** section:
  - URL: `/static/`
  - Directory: `/home/{username}/f1-encyclopedia/staticfiles/`
- Click **Add another**
- URL: `/media/`
- Directory: `/home/{username}/f1-encyclopedia/media/`

### 8. Reload & Visit
- Click **"Reload"** button
- Your site is now live at: `https://yourname.pythonanywhere.com`

## Done! 🎉

Your F1 Encyclopedia is online with:
✅ Free hosting
✅ Persistent database
✅ Admin panel to edit data
✅ Multiple projects support
