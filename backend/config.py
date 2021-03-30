class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://lotto:lottopassword@jiyoung-lotto-01.cjycxb02ponv.us-east-2.rds.amazonaws.com:3306/lotto'


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://lotto:lottopassword@jiyoung-lotto-01.cjycxb02ponv.us-east-2.rds.amazonaws.com:3306/lotto'