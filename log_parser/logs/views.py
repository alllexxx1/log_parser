from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from log_parser.logs.models import LogEntry
from log_parser.logs.serializers import LogEntrySerializer


class LogEntryPagination(PageNumberPagination):
    """
    Custom pagination class for LogEntry objects.

    This class sets a custom page size of 20 entries per page.
    """
    page_size = 20


class LogEntryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing LogEntry objects through the API.

    This class provides the standard create, retrieve, update, and delete (CRUD)
    operations for LogEntry objects via the Django REST Framework. It also supports
    filtering and pagination.
    """

    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('request_method', 'status_code', 'date')
    pagination_class = LogEntryPagination
