import sys, os, subprocess
INTERP = subprocess.check_output('pipenv --py', shell=True).strip().decode()
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
