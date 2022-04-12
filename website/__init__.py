from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']= 'can i pls die'

    from .veiws import veiws
    from .auth import auth

    app.register_blueprint(veiws, url_prefix= '/')
    app.register_blueprint(auth, url_prefix= '/')

    return app
