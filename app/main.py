from piccolo_admin.endpoints import AdminRouter
from starlette.routing import Mount, Router
from starlette.testclient import TestClient
from starlette.types import Receive, Scope, Send
from starlite import Starlite, asgi

from app.schema import Band, Manager

# Piccolo Admin asgi app
piccolo_admin = AdminRouter(Band, Manager)


@asgi(path="/admin")
async def admin(scope: Scope, receive: Receive, send: Send) -> None:
    """Asgi router, returns Piccolo Admin ASGI app."""
    scope["root_path"] = scope["path"]
    scope["path"] = "/"
    await piccolo_admin(scope, receive, send)


router = Router([Mount(path="/admin", app=piccolo_admin)])
app = Starlite(debug=True, route_handlers=[admin], openapi_config=None)


if __name__ == "__main__":
    # for running through debugger
    with TestClient(app=app) as client:
        client.get("/admin")

# To run through uvicorn:

# starlite
# $ poetry run uvicorn app.main:app --reload --reload-dir "." --reload-dir "../starlite/starlite/"

# starlette
# $ poetry run uvicorn app.main:router --reload --reload-dir "./app" --reload-dir "../starlite/starlite/"
