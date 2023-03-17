from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/0')
