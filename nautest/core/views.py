"""Define main views for core application."""
import json

import requests
from django.conf import settings as global_settings
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import QueryLog
from .utils import query_string_osm
from nautest.core.serializers import QueryLogSerializer
from nautest.core.serializers import UserSerializer


def _setHeaders():
    return {""}


class NearbyRestaurantsView(APIView):
    """API endpoint that allow nearby restaurants to be getted."""

    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Override the queryset definition."""
        location = self.request.query_params.get("location", None)

        if location is not None:
            ql = QueryLog(query_string=location)
            ql.save()

            req_headers = {
                "Content-Type": "application/xml",
                "Accept": "application/json",
            }
            res_headers = {"Content-Type": "application/json"}

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


class QueryLogViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Query Log to be readed."""

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = QueryLogSerializer
    http_method_names = ["get", "options"]

    def get_queryset(self):
        """Override the queryset definition."""
        return QueryLog.objects.all().order_by("-created_at")
