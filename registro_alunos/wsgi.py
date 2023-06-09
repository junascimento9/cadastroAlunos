from flask import Flask
from .routes import app_blueprint
from .config import app, db

app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    app.run(debug=True)


