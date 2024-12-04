import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:TBgj832M0HNMMMJs@localhost/db_componentsync')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'smtplaravel2019@gmail.com'
    MAIL_PASSWORD = 'puwvxfcgdzluqqrb'
    SECURITY_PASSWORD_SALT = 'puwvxfcgdzluqqrb'
