import os


folder = os.path.dirname(os.path.abspath(__file__))


dbfile = "todo_db.sqlite"


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)

class ProductionConfig(Config):
    DEBUG = False
    DB_FILE = os.path.join(folder,dbfile)

class StagingConfig(Config):
    DEBUG = True
    DB_FILE = os.path.join(folder,dbfile)

class DevelopmentConfig(Config):
    DB_FILE = os.path.join(folder, dbfile)
    try:
        os.remove(DB_FILE)
    except:
        pass

    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DB_FILE = ":memory:"