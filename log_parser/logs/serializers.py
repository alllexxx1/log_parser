from rest_framework import serializers
from log_parser.logs.models import LogEntry


class LogEntrySerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing Logs entries.

    This serializer converts LogEntry model instances into
    JSON format and specifies the fields to include.
    """

    class Meta:
        """This class specifies metadata options for the serializer."""
        model = LogEntry
        fields = '__all__'
