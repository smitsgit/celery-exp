from celery import Celery
from kombu import Queue

# app = Celery('tasks', broker='amqp://test:test@localhost:5672/test_vhost', backend='redis://localhost:6379/0')

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


CELERY_CONFIG = {
    'CELERY_DEFAULT_QUEUE': 'default',
    'CELERY_QUEUES': (Queue('default'), Queue('dev'),)
}

app.conf.update(**CELERY_CONFIG)