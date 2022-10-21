from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import home, NewsCreateAPIView

urlpatterns = [
    path('', home, name="name"),
    path('news/create/', NewsCreateAPIView.as_view(), name="create"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
