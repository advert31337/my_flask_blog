from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    context = {
        'title': 'Ошибка 404'
    }
    return render_template('errors/404.html', context=context), 404


@errors.app_errorhandler(403)
def error_403(error):
    context = {
        'title': 'Ошибка 403'
    }
    return render_template('errors/403.html', context=context), 403


@errors.app_errorhandler(500)
def error_500(error):
    context = {
        'title': 'Ошибка 500'
    }
    return render_template('error/500.html', context=context), 500