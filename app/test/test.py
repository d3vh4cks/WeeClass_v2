from flask import Blueprint

from app.module import dbModule

test = Blueprint('test', __name__, url_prefix='/test')

@test.route('/select')
def index():
  db_class = dbModule.Database()

  sql = 'select * from users'
  row = db_class.executeAll(sql)

  return row