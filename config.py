class Config(object):
    # Where to find the templates to build the pages from
    TEMPLATE_ROOT = 'templates/default/' # folder containing current template relative to app folder

    DEBUG = True
    DEVELOPMENT = True

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
