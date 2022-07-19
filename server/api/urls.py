from rest_framework import routers

from api.views import BaseModelViewSet

router = routers.SimpleRouter()

urlpatterns = []

router.register(r'base', BaseModelViewSet, basename='base')

urlpatterns += router.urls
