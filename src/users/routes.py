# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from src import db, bcrypt
from src.models import User, Post
from src.users.forms import (RegistrationForm, LoginForm, UpdateProfileForm,
                            RequestResetForm, ResetPasswordForm)
from src.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.hello'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Регистрация аккаунта {form.username.data} завершена!'
        'Теперь вы можете войти в систему', 'success')
        return redirect(url_for('users.login'))
    context = {'title': 'Регистрация нового пользователя'}
    return render_template('register.html', context=context, form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.hello'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data) 
            next_page = request.args.get('next')
            
            flash(f'Вы в системе.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.hello'))
        else:
            flash(f'Не смогли войти. Проверьте логин или пароль.', 'danger')
    context = {'title': 'Вход'}
    return render_template('login.html', context=context, form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.hello'))

@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Данные профиля обновлены.', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/%s' % current_user.image_file)
    context = {
        'title': 'Account',
        'image_file': image_file
    }
    return render_template('account.html', context=context, form=form) 

    
@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    context = {
        'posts': posts,
        'user': user
    }
    return render_template('user_posts.html', context=context)

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.hello'))  
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('На вашу почту отправлено письмо с инструкциями', 'info')
        return redirect(url_for('users.login'))

    context = {
        'title': 'Восстановление пароля',
        
    }
    return render_template('reset_request.html', context=context, form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.hello'))  
    user = User.verify_reset_token(token)
    if user is None:
        flash('Срок действия ссылки истек')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Пароль успешно изменен! Можете войти в систему', 'success')
        return redirect(url_for('users.login'))
    context = {
        'title': 'Новый пароль',
        'form': form
    }
    return render_template('reset_token.html', context=context, form=form)