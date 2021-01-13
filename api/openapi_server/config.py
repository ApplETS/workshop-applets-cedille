from os import environ


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://" + environ.get('DB_USER', 'root') + ":" + environ.get(
        'DB_PASSWORD', 'root_pass') + "@" + environ.get("DB_HOST", 'localhost') + ":" + environ.get("DB_PORT", '3306') + "/" + environ.get("DB_NAME",
                                                                                                                                           'db')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root_pass@localhost:3306/api_database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
