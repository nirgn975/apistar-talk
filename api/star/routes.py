from apistar import Route
from api.star.view import get, post, get_one, put, delete

routes = [
    Route('/', 'GET', get),
    Route('/', 'POST', post),
    Route('/{star_id}', 'GET', get_one),
    Route('/{star_id}', 'PUT', put),
    Route('/{star_id}', 'DELETE', delete),
]
