from datetime import datetime
from news.models import News
from src import db
import requests
from bs4 import BeautifulSoup



def get_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        
        result = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time')['datetime']
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
        return result
    return False
        


def get_html(url):
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except(requests.RequestException, ValueError):
            return False

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news_ = News(title=title, url=url, published=published)
        db.session.add(news_)
        db.session.commit()

if __name__ == '__main__':
    news = get_news(html)
    print(news)