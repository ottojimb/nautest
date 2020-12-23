"""nautest URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from nautest.core import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"query_logs", views.QueryLogViewSet, basename="query_log")

urlpatterns = [
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/nearby_restaurants/",
        views.NearbyRestaurantsView.as_view(),
        name="nearby_restaurants",
    ),
    path("api/", include(router.urls), name="api"),
    path("admin/", admin.site.urls),
]
