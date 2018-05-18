class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://bandanadee:'
        'thepassword'
        '@bandanadee.mysql.pythonanywhere-services.com/'
        'bandanadee$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'seeecreeet'