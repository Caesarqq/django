import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

app = Celery('web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks([
    'shop.tasks.py',
],force=True)

app.conf.beat_schedule = {
    'send-spam-every-55-minute': {
        'task': 'shop.tasks.send_beat_mail',
        'schedule': crontab(minute='*/55')
    },
}