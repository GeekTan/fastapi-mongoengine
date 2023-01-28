import collections
import contextvars
from contextlib import contextmanager
from typing import Dict

from fastapi import FastAPI
from mongoengine import connect, ConnectionFailure
from pymongo import MongoClient

__all__ = (
    "FastApiMongoEngine",
    "get_mongo_session",
)

from fastapi_mongoengine.extend import document

connections: contextvars.ContextVar[MongoClient] = contextvars.ContextVar("connections")


class FastApiMongoEngine:
    app: FastAPI
    config: Dict

    def __init__(self, app: FastAPI = None, config: Dict = None):
        connections.set(collections.defaultdict(dict))
        self.Document = document.ExtendDocument
        self.DynamicDocument = document.ExtendDynamicDocument

        if app is not None and config is not None:
            self.init_app(app, config)

    def init_app(self, app: FastAPI, config: Dict):
        if not app or not isinstance(app, FastAPI):
            raise TypeError("Invalid FastAPI application instance")
        self.app = app
        self.config = config
        self.app.add_event_handler("startup", self._connect_mongo)

    def _connect_mongo(self):
        for alias in self.config.keys():
            conn = connections.get()
            conn[alias] = connect(alias=alias, **self.config.get(alias))
            connections.set(conn)


@contextmanager
def get_mongo_session(alias: str):
    conn = connections.get()[alias]
    if isinstance(conn, dict):
        raise ConnectionFailure(f"Cannot connect to database {alias} :\n")

    with conn.start_session(causal_consistency=True) as session:
        yield session
