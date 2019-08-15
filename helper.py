# -*- coding: utf-8 -*-
import requests


def get_offers():
    webmaster_id = '56343448'
    token = 'sadfdsa'
    url = f'http://m1-shop.ru/offers_export_api/?webmaster_id={webmaster_id}&api_key={token}'
    
    r = requests.get(url).json()
    return r


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Victor Miroshnikov',
        'title': 'Как я настраиваю контекстную рекламу',
        'content': 'Тут все просто, берешь и делаешь',
        'date_posted': 'August 20, 2019'
    }
]