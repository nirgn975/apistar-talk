from apistar.frameworks.asyncio import ASyncIOApp as App
from api.routes import routes

from config.config import env

settings = {
    'DATABASE': {
        'URL': env['DATABASE_URL']
    }
}

app = App(routes=routes, settings=settings)


if __name__ == '__main__':
    app.main()
