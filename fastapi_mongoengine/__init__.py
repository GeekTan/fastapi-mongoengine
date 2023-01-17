import mongoengine
from fastapi import FastAPI

from fastapi_mongoengine.connection import create_connections

global connections


class MongoEngine:
    def __init__(self, app: FastAPI = None, config=None):
        self.app = app
        self.config = config
        if app is not None:
            self.init_app(app, config)

    def init_app(self, app: FastAPI, config=None):
        if not app or not isinstance(app, FastAPI):
            raise TypeError("Invalid FastAPI application instance")
        self.app = app
        app.add_event_handler("startup", self._init_app(config))

    def _init_app(self, config):
        global connections
        connections = create_connections(config)

    def __getattr__(self, attr_name):
        return getattr(mongoengine, attr_name)


async def get_mongoengine():
    return connections
