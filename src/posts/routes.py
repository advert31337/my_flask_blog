# -*- coding: utf-8 -*-
from flask import (Blueprint, render_template, url_for, flash,
                    redirect, request, abort)
from flask_login import current_user, login_required
from src import db
from src.models import Post, Tag
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
    tags = post.tags
    context= {
        'title': post.title,
        'post' : post,
        'tags' : tags
    }
    return render_template('post.html', context=context)


@posts.route('/post/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_datail', post=post, tags=tags)





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

@posts.route('/tag/<slug>')
def tag_detail(slug):
    page = request.args.get('page', 1, type=int)
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    print(posts)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render_template('tag_detail.html', context=context)

