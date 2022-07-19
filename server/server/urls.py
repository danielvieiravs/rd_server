"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from drf_yasg.views import SwaggerUIRenderer, get_schema_view
from drf_yasg import openapi

from api import urls as api_urls

SwaggerUIRenderer.template = 'drf-yasg/swagger-ui.html'

api_patterns = [
    path('api/1.0/', include([path('', include(api_urls))])),
]


schema_view = get_schema_view(
    openapi.Info(
        title='RN API documentation',
        default_version='v1',
        contact=openapi.Contact(name='RN', email='support@rn.com'),
    ),
    patterns=api_patterns,
    url=settings.BASE_URL + '/api/1.0/',
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        'api-docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='api_docs_v2',
    ),
    path(
        'api/1.0/',
        include((api_urls, 'api'), namespace='api_v1'),
    ),
    path('admin/', admin.site.urls),
]
