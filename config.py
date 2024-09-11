import os

class Config:
  WEECLASS_DB = os.getenv('WEECLASS_DB')
  WEECLASS_DB_USER = os.getenv('WEECLASS_DB_USER')
  WEECLASS_DB_PW = os.getenv('WEECLASS_DB_PW')