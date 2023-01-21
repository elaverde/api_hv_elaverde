from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
# Crea un objeto engine
User = str(os.environ.get("USERBD"))
Password = str(os.environ.get("PASSWORDBD"))
Host = str(os.environ.get("HOST"))
BD = str(os.environ.get("BD"))

engine = create_engine("mysql://"+User+":"+Password+"@"+Host)
# Verifica si la base de datos "elaverde" existe
result = engine.execute("SHOW DATABASES").fetchall()
databases = [x[0] for x in result]
if BD not in databases:
    engine.execute("CREATE DATABASE "+BD)
# Crea un objeto db

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://"+User+":"+Password+"@"+Host+"/"+BD+"?charset=utf8mb4"
db = SQLAlchemy(app)