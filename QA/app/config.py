import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration variables as needed


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # Add other production configurations here

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:juan@127.0.0.1:5432/ejer_final'
    # O la configuración adecuada para tu base de datos de prueba

class CoverageConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:juan@127.0.0.1:5432/ejer_final'
    COVERAGE = True
    COVERAGE_DIR = os.path.join(basedir, 'coverage')  

# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "coverage": CoverageConfig,
    # Add other environments if needed
}



