# -*- coding: utf-8 -*-
from flask import (Blueprint, render_template, url_for, flash,
                    redirect, request, abort)
from flask_login import current_user, login_required
from src import db
from src.models import Post
from src.posts.forms import PostForm


posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Запись размещена', 'success')
        return redirect(url_for('main.hello'))

    context = {
        'title': 'Новая запись',
        'legend': 'Новая запись'
    }
    return render_template('create_post.html', context=context, form=form)


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    context= {
        'title': post.title,
        'post' : post
    }
    return render_template('post.html', context=context)


@posts.route('/post/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/post_datail', post=post)





@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Запись изменена', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    context = {
        'title': 'Редактирование записи',
        'legend': 'Редактирование записи'
    }
    return render_template('create_post.html', context=context, form=form)

@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Запись удалена', 'success')
    return redirect(url_for('hello'))
