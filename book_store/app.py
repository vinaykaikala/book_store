import logging.config
import click
from flask import Flask, Blueprint

from book_store import settings
from book_store.api.store.endpoints.books import ns as book_store_namespace
from book_store.api.restplus import api
from book_store.database import db

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(book_store_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@click.command()
@click.option('-p', '--port', type=int, default=5000)
def main(port):
    initialize_app(app)
    logging.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format('localhost'))
    app.run(host="0.0.0.0", debug=settings.FLASK_DEBUG, port=port)
