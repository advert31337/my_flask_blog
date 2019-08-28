from flask import (render_template, request, Blueprint, abort, 
                    current_app, request, redirect, url_for, flash)
from flask_login import current_user, login_required

from src import db
from .models import News, Comment
from .handler import get_news
from .forms import CommentForm
from src.utils import get_redirect_target

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
    comment_form = CommentForm(news_id=article.id)
    context = {
        'title': article.title,
        'article': article,
        'comment_form': comment_form
    }
    return render_template('news/news_article.html', context=context)

@login_required
@news.route('/news/comment', methods=['POST'])
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, 
                            news_id=form.news_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен') 
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(
                    getattr(form, field).label.text,
                    error
                ))   
    return redirect(get_redirect_target())                