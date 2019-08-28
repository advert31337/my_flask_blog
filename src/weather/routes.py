from flask import render_template, request, Blueprint
from .get_weather import weather_by_city

weather = Blueprint('weather', __name__)


@weather.route('/weather')
def weather_info():
    w = weather_by_city('rostov-on-don')
    context = {
        'title': 'Погода'
    }
    return render_template('weather/index.html', context=context, weather=w)
    