from flask import Flask
from extensions import db,jwt
from config import Config
from routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(task_bp, url_prefix= '/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)