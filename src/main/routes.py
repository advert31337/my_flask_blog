from flask import render_template, request, Blueprint
from src.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def hello():
    q = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    if q:
        context = Post.query.filter(Post.title.contains(q) | Post.content.contains(q)).paginate(page=page, per_page=5)
    else:
        context = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', context=context)

@main.route('/about')
def about():
    context = {'title': 'Обо мне'}
    return render_template('about.html', context=context)