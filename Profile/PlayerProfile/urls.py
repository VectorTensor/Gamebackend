
from django.urls import path, include
from .routers import router


urlpatterns = [

        # path('', TestView),
        path('',include(router.urls))

]





