# -*- coding: utf-8 -*-
from os import path

class Config(object):
    DEBUG = False
    TESTING = False
    ROOT_DIR = path.abspath(
        path.dirname(path.join(__file__))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/test.db' % (ROOT_DIR)
    SECRET_KEY='\x62\x27\x5c\x78\x39\x30\x5c\x78\x65\x30\x26\x77\x45\x5c\x78\x65\x35\x5c\x78\x62\x30\x36\x5c\x78\x62\x61\x5c\x78\x61\x30\x5c\x78\x62\x35\x77\x5c\x78\x61\x39\x39\x7a\x5c\x78\x63\x63\x5c\x78\x38\x39\x5c\x78\x62\x65\x3d\x5c\x78\x30\x30\x5c\x72\x36\x7c\x5c\x78\x61\x65\x27'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/foo'
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_NATIVE_UNICODE = True
