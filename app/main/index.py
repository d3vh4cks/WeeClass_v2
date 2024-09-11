from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
  return 'mainPage'