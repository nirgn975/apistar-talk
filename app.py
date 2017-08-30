from apistar.frameworks.wsgi import WSGIApp as App

from api.routes import routes

from mongoengine import connect
connect('apistar-talk')

app = App(
    routes=routes,
)


if __name__ == '__main__':
    app.main()
