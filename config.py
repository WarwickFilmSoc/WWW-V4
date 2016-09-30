class Config(object):
    # Where to find the templates to build the pages from
    TEMPLATE_ROOT = 'templates/default/' # folder containing current template relative to app folder

    DEBUG = True
    DEVELOPMENT = True

    # Flask-SSO Configuration
    SSO_ATTRIBUTE_MAP = {
        'pid': (True, 'pid'),
        'givenName': (True, 'givenName'),
        'surname': (True, 'surname'),
        'username': (True, 'username'),
        'photo_id': (False, 'photo_id'),
        'mail': (True, 'mail'),
        'web_id': (True, 'web_id')
        }

    SSO_LOGIN_URL = '/login'		
    SSO_LOGIN_ENDPOINT = '/login/sso'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False