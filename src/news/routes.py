from flask import render_template, request, Blueprint
from .models import News
from .handler import get_news


news = Blueprint('news', __name__)


@news.route('/news')
def news_collect():
    n = News.query.order_by(News.published.desc()).all()
    context = {
        'title': 'Новости'
    }
    return render_template('news/index.html', context=context, news=n)