from src import create_app
from src.news.parsers import habr

app = create_app()
with app.app_context():
    #habr.get_news_snippets()
    habr.get_news_content()