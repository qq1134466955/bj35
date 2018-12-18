



# 配置类
import logging
from redis import StrictRedis


class Config(object):
    DEBUG = True
    SECRET_KEY = "2141414124"


# 创建数据库链接
    SQLALCHEMY_DATABASE_URI = 'musql://root:mysql@127.0.0.1:3306/bj35_py'
# 数据库追踪设置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2

class development_config(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
class production_config(Config):
    DEBUG = True
    LOG_LEVEL = logging.WARNING
class measurement_config(Config):
    DEBUG = True
config = {
    'development': development_config,
    'production' : production_config,
    'measurement': measurement_config
}