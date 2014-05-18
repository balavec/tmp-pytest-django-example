import os, sys

# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

# SETTINGS
DEBUG = TEMPLATE_DEBUG = True
ROOT_URLCONF = me
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': here('.') + '/example_db',
    }
}
TEMPLATE_DIRS = (here('.'), )
SECRET_KEY = 'whatever'
INSTALLED_APPS = ['django.contrib.auth', 'django.contrib.contenttypes']

# URLS
# urlpatterns = patterns('', (r'^(?P<name>\w+)?$', index))
urlpatterns = []

if __name__=='__main__':
    # set the ENV
    os.environ['DJANGO_SETTINGS_MODULE'] = me
    sys.path += (here('.'),)
    # run the development server
    from django.core import management
    management.execute_from_command_line() 
