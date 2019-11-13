from flask_restplus import fields
from book_store.api.restplus import api

search_result = api.model('BookStore', {
    'Title': fields.String(required=True, attribute='book_title', description='Book Title'),
    'Author' : fields.String(required=True, description='book_author'),
    'Category': fields.String(required=True, attribute='book_category', description='Book Category'),
    'Availability': fields.String(readOnly=True, attribute='book_availability', description='Book Availability'),
    'Year': fields.String(required=True, description='Book Published year'),
})

books_list = api.model('Books Result', {'items': fields.List(fields.Nested(search_result))})
