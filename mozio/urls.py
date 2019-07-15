"""mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from . import views
from .routers import HybridRouter
from api.views import *

router = HybridRouter()
router.register(r'polygons', GetPolygons, r"polygons")
router.add_api_view(r'auth', url(r'^auth/$', ObtainAuthToken.as_view(), name=r"auth"))

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^createprovider', CreateProvider.as_view(),name='createprovider'),
    url(r'^$', index_view, {}, name='index'),
]
