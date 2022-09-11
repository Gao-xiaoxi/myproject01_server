
class Config():
    # 数据库配置uri
    SQLALCHEMY_DATABASE_URI = 'mysql://root:abc123456@localhost/flask_ego'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'abcd123'