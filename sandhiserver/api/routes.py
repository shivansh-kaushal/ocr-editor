from .book import BooksApi, BookApi
from .bookresources import ImageApiHandler, HocrApiHandler


def initialize_routes(api):
    api.add_resource(BooksApi, '/books')
    api.add_resource(BookApi, '/books/<id>')
    api.add_resource(ImageApiHandler, '/i/b/<int:bid>/p/<int:pid>/')
    api.add_resource(HocrApiHandler, '/h/b/<int:bid>/p/<int:pid>/')
