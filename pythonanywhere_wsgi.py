"""
WSGI config for f1_site project on PythonAnywhere
"""
import os
import sys

# Add your project directory to sys.path
project_home = '/home/{username}/f1-encyclopedia'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'f1_site.settings'

# Import Django WSGI app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
