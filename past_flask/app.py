from flask import Flask,jsonify
from extensions import db, jwt
from config import Config
from routes import task_bp
from werkzeug.exceptions import HTTPException

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(task_bp, url_prefix='/api')

    
    def register_error_handlers(app):
        @app.errorhandler(Exception)
        def handle_exception(e):
            if isinstance(e, HTTPException):
                response = e.get_response()
                code = e.code
                message = e.description
            else:
                code = 500
                message = str(e)

            response = {
                "error": {
                    "code": code,
                    "message": message
                }
            }
            return jsonify(response), code

    register_error_handlers(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)






