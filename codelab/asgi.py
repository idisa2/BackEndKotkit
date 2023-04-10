"""
ASGI config for codelab project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import pal.routing
from pal import routing
# from pal.middlewares import WebSocketJWTAuthMiddleware
from pal.middleware_test import JwtAuthMiddlewareStack, TokenAuthMiddleware

"""
This routinng filee is not use, the  used one is codelab.routing

"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codelab.settings')

# application = get_asgi_application()
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
  "http": django_asgi_app,
    # "websocket": URLRouter(pal.routing.websocket_urlpatterns),

    # "websocket": WebSocketJWTAuthMiddleware(
    #     URLRouter(
    #         routing.websocket_urlpatterns
    #     )
    # ),

  "websocket": TokenAuthMiddleware(
    URLRouter(
      routing.websocket_urlpatterns
    )
  ),

})