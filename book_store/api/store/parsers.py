from flask_restplus import reqparse

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('author', type=str,  help='')
