JSON_AS_ASCII = False
DEBUG = True
SECRET_KEY = '77?1fj3n%='

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_flask_db'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = '451278643@qq.com'
MAIL_PASSWORD = 'mqwhogcwgqwnbiad'
MAIL_DEFAULT_SENDER = '451278643@qq.com'
