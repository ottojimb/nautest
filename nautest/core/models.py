"""Module to define models settings."""
from django.db import models


class QueryLog(models.Model):
    """Class to define the query log attributes."""

    query_string = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Set the query log description."""
        return f"{self.query_string} - {self.created_at}"
