import os

class Config:
    userbd = os.getenv('USERBD')
    password = os.getenv('PASSBD')
    host = os.getenv('HOST')
    port = os.getenv('PORTHTTP')
    database = os.getenv('DATABASE')
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(userbd, password, host, port, database)
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False