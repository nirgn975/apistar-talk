from apistar import Include
from apistar.handlers import docs_urls, static_urls

from api.star.routes import routes as star_routes

routes = [
    Include('/star', star_routes),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
