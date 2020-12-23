"""Define main views for core application."""
from django.conf import settings as global_settings
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from nautest.core.serializers import UserSerializer
from .utils import query_string_osm

import requests
import json


def _setHeaders():
    return {""}


class NearbyRestaurantsView(APIView):
    """API endpoint that allow nearby restaurants to be getted"""

    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Override the queryset definition."""
        location = self.request.query_params.get("location", None)

        if location is not None:
            req_headers = {"Content-Type": "application/xml", "Accept": "application/json"}
            res_headers={"Content-Type": "application/json"}

            req = requests.post(
                global_settings.OSM_PROVIDER,
                data=query_string_osm(location),
                headers=req_headers,
            )

            response = json.loads(req.text)
            return Response(response, headers=res_headers)


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows USERS to be created or edited."""

    serializer_class = UserSerializer
    http_method_names = ["post", "get", "options"]

    def get_queryset(self):
        """Override the queryset definition."""
        return User.objects.filter(id=self.request.user.id).order_by("id")
