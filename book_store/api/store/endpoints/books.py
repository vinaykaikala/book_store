import logging

from flask import request
from flask_restplus import Resource
from book_store.api.store.business import get_books
from book_store.api.store.serializers import search_result
from book_store.api.store.parsers import search_arguments
from book_store.api.restplus import api
from book_store.database.models import BookStore

log = logging.getLogger(__name__)

ns = api.namespace('books', description='Operations to gene search')


@ns.route('/')
@api.response(405, 'page not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'Found book information')
class BookSearch(Resource):
    #@api.expect(search_arguments,validate=True)
    #@api.marshal_list_with(search_result)
    def get(self):
        """
        Returns gene search result.
        * Send a JSON object with the new lookup  in the request body.
        ```
        {
        }
        ```
        """
        args = search_arguments.parse_args()
        return 'Working', 200
