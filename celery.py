from __future__ import absolute_import
import os

from celery import Celery
from kombu import Exchange, Queue

from .config import DefaultConfig


configuration = DefaultConfig
        
app = Celery('medusa',
    broker=configuration.CELERY_BROKER_URL,
    include=['tasks']
)
#Compose settigs
app.conf.BROKER_USE_SSL = configuration.BROKER_USE_SSL
app.conf.BROKER_CONNECTION_TIMEOUT = 30 # give DNS and network resolution some extra time
app.conf.CELERY_RESULT_BACKEND = None # AMQP is not recommended as result backend as it creates thousands of queues 
app.conf.CELERY_SEND_EVENTS = False # Will not create celeryev.* queues 
app.conf.CELERY_EVENT_QUEUE_EXPIRES = 60 # Will delete all celeryev. queues without consumers after 1 minute.
# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_DEFAULT_QUEUE='default',
    CELERY_ROUTES={
        'tasks.add_metric': {'queue': 'metrics'},
    },
    CELERY_QUEUES=(
        Queue('default', Exchange('default'), routing_key='default'),
        Queue('metrics', Exchange('metrics'), routing_key='tasks.add_metric'),
    )
)

if __name__ == '__main__':
    app.start()