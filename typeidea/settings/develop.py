from .base import * #NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',  # 数据库
        'USER': 'root',  # 账号
        'PASSWORD': '123456',  # 密码
        'HOST': '127.0.0.1',  # ip
        'PORT': '3306',  # 端口号
        'TEST_CHARSET': 'utf-8'
    }
}
