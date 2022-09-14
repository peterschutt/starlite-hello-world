from starlite.testing import TestClient

from app.main import app


def test_app() -> None:
    with TestClient(app=app) as client:
        assert client.get("/").json() == {"hello": "world"}
