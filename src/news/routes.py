from flask import render_template, request, Blueprint
from src.models import Post
from .handler import get_news

news = Blueprint('news', __name__)


@news.route('/news')
def news_collect():
    n = get_news()
    context = {
        'title': 'Новости'
    }
    return render_template('news/index.html', context=context, news=n)