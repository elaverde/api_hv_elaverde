from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
from flask_sslify import SSLify

from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
sslify = SSLify(app)

# Crea un objeto engine
User = str(os.environ.get("USERBD"))
Password = str(os.environ.get("PASSBD"))
Host = str(os.environ.get("HOST"))
BD = str(os.environ.get("BD"))


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://"+User+":"+Password+"@"+Host+":5050"+"/"+BD+"?charset=utf8mb4"
db = SQLAlchemy(app)