from django.urls import path
from .consumers import NewsConsumer

websocket_urlpatterns = [
    path("ws/news/", NewsConsumer.as_asgi()),
]
