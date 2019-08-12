# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from src.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', 
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя уже занято! Попробуйте другое.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Эта почта уже занята! Попробуйте другое.')

class LoginForm(FlaskForm):
    email = StringField('Почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Оставаться в системе')
    submit = SubmitField('Войти')


class UpdateProfileForm(FlaskForm):
    username = StringField('Имя пользователя', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Почта',
                        validators=[DataRequired(), Email()])
    picture = FileField('Поменять изображение профиля', validators=[FileAllowed(['jpeg', 'jpg', 'png'])])
    submit = SubmitField('Обновить')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Это имя уже занято! Попробуйте другое.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Эта почта уже занята! Попробуйте другое.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Сбрость пароль')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Нет такой почты в сервисе. Зарегистрируйстесь!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', 
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Измениту пароль')