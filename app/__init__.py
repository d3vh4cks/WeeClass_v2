from flask import Flask
from config import Config

app = Flask(__name__)

from app.main.index import main
from app.test.test import test

app.register_blueprint(main)
app.register_blueprint(test)