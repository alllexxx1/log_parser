from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from log_parser.logs.models import LogEntry
from log_parser.logs.serializers import LogEntrySerializer


class LogEntryPagination(PageNumberPagination):
    page_size = 20


class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('request_method', 'status_code', 'date')
    pagination_class = LogEntryPagination
