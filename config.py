"""Configuration definition module

This file is used to manage application confiugrations. These can include
development, testing, staging, and production configurations. These different
configuration may set different database uris, application setttings, error reporting
modes, etc.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
