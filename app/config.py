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
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/ejer_final'

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@0.0.0.0:5432/ejer_final'
    # Configuración para la base de datos de producción

config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

