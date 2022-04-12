from flask import Blueprint

veiws = Blueprint('veiws', __name__)

@veiws.route('/')
def home():
    return "<h1>Test</h1>"