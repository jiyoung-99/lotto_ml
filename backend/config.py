class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://jiyoung:lottopassword@localhost:3307/lotto'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://jiyoung:lottopassword@localhost:3307/lotto'