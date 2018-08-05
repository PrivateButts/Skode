import sys, os, subprocess

# Import local environmental varbs
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / 'local.env'
load_dotenv(dotenv_path=env_path)
load_dotenv()

INTERP = os.getenv('PYTHON_PATH')
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/src')

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python3.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "Skode.settings"
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from django.core.wsgi import get_wsgi_application
wsgi_application = get_wsgi_application()

def application(environ, start_response):
    if environ['wsgi.url_scheme'] == 'http':
        url = 'https://' + environ['HTTP_HOST'] + environ['REQUEST_URI']
        start_response('301 Moved Permanently', [('Location', url)])
        return []

    return wsgi_application(environ, start_response)

application = Sentry(application)
