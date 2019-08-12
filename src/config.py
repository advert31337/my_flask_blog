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
    MAIL_PASSWORD = 'mvic2902228*0255'#os.environ.get('EMAIL_PASS')