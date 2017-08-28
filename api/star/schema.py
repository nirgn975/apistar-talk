from apistar import typesystem


class RatingSchema(typesystem.Integer):
    minimum = 1
    maximum = 5


class SizeSchema(typesystem.Enum):
    enum = ['small', 'medium', 'large']


class StarSchema(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
        'rating': RatingSchema,
        'dimension': SizeSchema,
    }
