import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = 'Flask App'
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Ensure you set a secret key, this is important!')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass 


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get(
    #    'DEVEL_DATABASE_URL', 'sqlite:///' + os.path.join(base_dir, 'database-devel.db'))
    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost/ls'


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL', 'sqlite:///' + os.path.join(base_dir, 'database-test.db'))


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///' + os.path.join(base_dir, 'database.db'))
    #SQLALCHEMY_DATABASE_URI = 'mysql://login:password@localhost/lexale39_wh'
    #SQLALCHEMY_POOL_RECYCLE = 10
    WTF_CSRF_ENABLED = True


config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig)
