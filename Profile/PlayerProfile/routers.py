
from rest_framework import routers
from .views import ProfileViewSet

router = routers.DefaultRouter()

router.register(r'api/v1/Profiles',ProfileViewSet)

