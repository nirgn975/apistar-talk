import typing
import json
from apistar import Response
from apistar import http

from api.star.schema import StarSchema
from api.star.model import Star


def get() -> typing.List[StarSchema]:
    """
    Get all the stars.
    """
    stars = Star.objects.to_json()
    return Response(stars, status=200, headers={'content-type': 'application/json'})


def post(new_star: StarSchema) -> StarSchema:
    """
    Create a new star.
    """
    saved_star = Star(**new_star)
    saved_star.save()
    return Response(saved_star.to_json(), status=201, headers={'content-type': 'application/json'})


def get_one(star_id: str) -> StarSchema:
    """
    Get star by id.
    """
    star = Star.objects(id=star_id)
    return Response(star.to_json(), status=200, headers={'content-type': 'application/json'})


def put(star_id: str, new_star: StarSchema) -> StarSchema:
    """
    Edit a star by id.
    """
    star = Star.objects.get(id=star_id)
    star.modify(**new_star)
    star.save()
    return Response(star.to_json(), status=200, headers={'content-type': 'application/json'})


def delete(star_id: str) -> StarSchema:
    """
    Delete a star by id.
    """
    star = Star.objects.get(id=star_id)
    star.delete()
    return Response(star.to_json(), status=200, headers={'content-type': 'application/json'})
