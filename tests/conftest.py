import pytest
import uvicorn
from fastapi import FastAPI
from starlette.testclient import TestClient

from fastapi_mongoengine import get_mongo_session
from fastapi_mongoengine.extend.collection import ExtendCollection
from tests.model import UserModel, User, db


def _create_app() -> FastAPI:
    _app = FastAPI()
    db.init_app(_app, {
        "test_db": {
            "host": "mongodb://127.0.0.1:27017/test_db"
        }

    })
    return _app


app = _create_app()


@app.get("/")
async def read_user(name: str):
    user = User.objects(name=name).first()
    return user.id


@app.post("/")
def create_user(user: UserModel):
    user_collection = ExtendCollection(User)
    with get_mongo_session("test_db") as session:
        user_collection.insert_one(User(name=user.name, phone=user.phone), session)
    return "succeed"


@pytest.fixture
def http_client() -> TestClient:
    return TestClient(app)


if __name__ == "__main__":
    uvicorn.run(app)
