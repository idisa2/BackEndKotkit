import os

# from websocket.middlewares import WebSocketJWTAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from pal import routing
from pal.middleware_test import TokenAuthMiddleware

from pal.middlewares import WebSocketJWTAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codelab.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WebSocketJWTAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
        # "websocket": TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
        # "websocket": URLRouter(routing.websocket_urlpatterns),
        # "websocket": routing.websocket_urlpatterns,
    }
)
