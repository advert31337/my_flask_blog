from flask import render_template, request, Blueprint, abort, current_app
from .models import News
from .handler import get_news


news = Blueprint('news', __name__)


@news.route('/news')
def news_collect():
    n = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    context = {
        'title': 'Новости'
    }
    return render_template('news/index.html', context=context, news=n)


@news.route('/news/<int:news_id>')
def news_article(news_id):
    article = News.query.filter(News.id == news_id).first()
    if not article:
        abort(404)
    
    context = {
        'title': article.title,
        'article': article
    }
    return render_template('news/news_article.html', context=context)
