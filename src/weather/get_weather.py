import requests
from config import Config



def weather_by_city(city_name):
    if not city_name:
        city_name = current_app.config['WEATHER_DEFAULT_CITY']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format':'json',
        'num_of_days':1,
        'lang': 'ru'
    }

    url = f'http://api.worldweatheronline.com/premium/v1/weather.ashx?'
    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
        weather = r.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('ошибка соединения')
        return False
    return False  # print(r['data']['current_condition'][0])

if __name__ == '__main__':
    w = weather_by_city('rostov-on-don')
    print(w)