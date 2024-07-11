
from rest_framework import routers
from .views import ProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router = routers.DefaultRouter()

router.register(r'v1/Profiles',ProfileViewSet)


