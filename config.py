# -*- coding: utf-8 -*-

import os
from utils import make_dir, INSTANCE_FOLDER_PATH
from datetime import timedelta


class BaseConfig(object):
    PROJECT = "medusa"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = False
    ADMINS = ['gloria@sentinel.la']
    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

class DefaultConfig(BaseConfig):
    DEBUG = True
    # InfluxDB
    INFLUX_HOST = 'influx'
    INFLUX_PORT = 8086
    INFLUX_DB = 'sentinella'
    INFLUX_USER = 'admin'
    INFLUX_PASSWORD = 'admin'
    INFLUX_USE_SSL = False

    #Celery
    CELERY_BROKER_URL = 'amqp://admin:admin@amq//'
    CELERY_BACKEND_URL = 'amqp://admin:admin@amq//'
    BROKER_USE_SSL = False
  


