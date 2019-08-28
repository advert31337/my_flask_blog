<<<<<<< HEAD
import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)
class Config:
    SECRET_KEY = 'a24316beadadff2c538006d54a0dcea80dafd52b8d35d04da8'#os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/site.db' #os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'adv31337@gmail.com'#os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = '4544454845fdsfjkjeiII(*kkkj'#os.environ.get('EMAIL_PASS')

    WEATHER_DEFAULT_CITY = 'Moscow.Russia'
    WEATHER_API_KEY = 'a3204219c1cc4d5c9a0101253191508'
=======
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "site.db")

class Config:
    SECRET_KEY = 'a24316beadadff2c538006d54a0dcea80dafd52b8d35d04da8'#os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}' #os.environ.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'adv31337@gmail.com'#os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = '4544454845fdsfjkjeiII(*kkkj'#os.environ.get('EMAIL_PASS')
>>>>>>> 8fa2bb94e06fb43aac0215c9a5fc5e596804c71b
