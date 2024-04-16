"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path
from drf_yasg.generators import OpenAPISchemaGenerator

MODE = 'DEV'

class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema.basePath = '/Samples/'
        return schema
GENERATOR_CLASS = CustomOpenAPISchemaGenerator

schema_view = get_schema_view(
    info=openapi.Info(
        title="CBK TRIAL APIs",
        default_version='v1',
        description="APIs made to Retrieve and Post reports on a given period of time on CBK Endpoints",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="nyamburaajanee@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=GENERATOR_CLASS,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Samples/',include('Samples.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    ]
