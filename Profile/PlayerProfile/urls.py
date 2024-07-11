
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .routers import router


urlpatterns = [
        # path('', TestView),
        path('api/',include(router.urls)),
        path('api/token/',TokenObtainPairView.as_view(), ),
        path('api/token/refresh/',TokenRefreshView.as_view())

]





