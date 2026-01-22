import os

SECRET_KEY = "sdfsdfk2rjl23"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "media")
if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)
    print(f"创建媒体目录: {MEDIA_DIR}")

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'zzh2864799'
MYSQL_DATABASE = 'vegetable_provider'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4'


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3529223875@qq.com"
MAIL_PASSWORD = "dhjbeoylyiffdbcd"
MAIL_DEFAULT_SENDER = "3529223875@qq.com"