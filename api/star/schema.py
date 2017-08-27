from apistar import typesystem


class Rating(typesystem.Integer):
    minimum = 1
    maximum = 5


class Size(typesystem.Enum):
    enum = ['small', 'medium', 'large']


class Star(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
        'rating': Rating,
        'size': Size,
    }
