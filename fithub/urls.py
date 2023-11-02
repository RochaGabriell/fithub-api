"""
URL configuration for fithub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="Infinity Fire solution APIs",
        default_version='v0.2.0',
        description="Welcome to the API Documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # Swagger e Redoc
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Apps
    path('api/v1/account/', include('fithub.apps.account.urls'), name="account"),
    path('api/v1/exercise/', include('fithub.apps.exercise.urls'), name="exercise"),
    path('api/v1/manager/', include('fithub.apps.manager.urls'), name="manager"),
]
