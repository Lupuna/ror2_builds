from django.urls import path, include
from rest_framework import routers
from builds.views import BuildView

router = routers.DefaultRouter()
router.register(r'', BuildView)

urlpatterns = [
    path('', include(router.urls))
]
