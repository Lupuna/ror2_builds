from django.urls import path, include
from rest_framework import routers
from items.views import AddonView, ItemView

router = routers.DefaultRouter()
router.register(r'api/addons', AddonView)
router.register(r'api/items', ItemView)

urlpatterns = [
    path('', include(router.urls))
]
