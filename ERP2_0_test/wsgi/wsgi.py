import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ERP2_0_test.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path=os.path.dirname(os.path.abspath(__file__))
path=path+"/../.."
if path not in sys.path:
    sys.path.append(path)
