import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carnepal.settings')

app = Celery('carnepal', result_extended=True) 

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule =[

]

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')