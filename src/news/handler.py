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
            result.append({
                'title': title,
                'url': url,
                'published': published
            })
        return result
    return False
        


def get_html(url):
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except(requests.RequestException, ValueError):
            return False


if __name__ == '__main__':
    news = get_news(html)
    print(news)