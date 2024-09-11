import os
from dotenv import load_dotenv

class Config:
  WEECLASS_DB = ''
  WEECLASS_DB_USER = ''
  WEECLASS_DB_PW = ''
  
  def load_config():
    load_dotenv()
    Config.WEECLASS_DB = os.getenv('WEECLASS_DB') 
    Config.WEECLASS_DB_USER = os.getenv('WEECLASS_DB_USER')
    Config.WEECLASS_DB_PW = os.getenv('WEECLASS_DB_PW')