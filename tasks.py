from celery import Celery
from celery.schedules import crontab

from src import create_app
from src.news.parsers import habr

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')



# celery -A tasks worker --loglevel=info
#  set FORKED_BY_MULTIPORCESSING=1 && celery -A tasks worker --loglevel=info
@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()
        
@celery_app.task
def habr_content():
    with flask_app.app_context():
        habr.get_news_content()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1', habr_snippets.s()))
    sender.add_periodic_task(crontab(minute='*/1', habr_content.s()))