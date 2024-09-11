from app import app, Config

if __name__ == '__main__':
  Config.load_config()
  app.run(host='127.0.0.1', port=4445)