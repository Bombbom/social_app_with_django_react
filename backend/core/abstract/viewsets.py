from rest_framework import viewsets
from rest_framework import filters
class AbstractViewSet(viewsets.ModelViewSet):
    """
    AbstractViewSet inheritance from rest_framework.viewsets.ModelViewSet.
    
    """
    ordering_fields = ["updated", "created"]
    ordering = ["-updated"]