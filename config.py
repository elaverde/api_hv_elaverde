import os

class Config:
    userbd = os.getenv('USERBD', 'root')
    password = os.getenv('PASSBD', '')
    host = os.getenv('HOST', 'localhost')
    port = os.getenv('PORTHTTP', '3306')
    database = os.getenv('DATABASE', 'db_hv_elaverde')
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(userbd, password, host, port, database)

    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-super-secret-key')