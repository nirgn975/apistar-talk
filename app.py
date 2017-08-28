from apistar.frameworks.asyncio import ASyncIOApp as App

from api.routes import routes

from mongoengine import connect
connect('apistar-talk')

app = App(
    routes=routes,
)


if __name__ == '__main__':
    app.main()
