from rest_framework import permissions, viewsets


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get']
