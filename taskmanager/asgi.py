"""
ASGI config for todo6 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from channels import routing

from django.core.asgi import get_asgi_application

from channels.sessions import CookieMiddleware, SessionMiddleware









os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    # "websocket": CookieMiddleware(SessionMiddleware(URLRouter(routing.websocket_urlpatterns))),
})
