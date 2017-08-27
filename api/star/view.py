import typing
from apistar import Response
from apistar import http


from api.star.schema import Star

_items: typing.List[typing.Tuple[int, Star]] = []

def get() -> typing.List[Star]:
    """
    Get all the stars.
    """
    return [Star(item[1]) for item in _items]


def post(new_star: Star) -> Star:
    """
    Create a new star.
    """
    _items.append((len(_items), new_star))
    return Star(new_star)


def get_one(star_id: int) -> Star:
    """
    Get star by id.
    """
    return Star(_items[star_id - 1][1])


def put(star_id: int, new_star: Star) -> Star:
    """
    Edit a star by id.
    """
    _items[star_id - 1][1].update(new_star)
    return Star(_items[star_id - 1][1])


def delete(star_id: int) -> Star:
    """
    Delete a star by id.
    """
    deleted_star = _items.pop((star_id - 1))
    return Star(deleted_star[1])
