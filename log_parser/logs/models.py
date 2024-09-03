from django.db import models


class LogEntry(models.Model):
    """"
    Model representing a single log entry from an Nginx log file.
    """

    ip_address = models.GenericIPAddressField()
    request_method = models.CharField(max_length=10)
    request_uri = models.CharField(max_length=255)
    status_code = models.IntegerField()
    bytes_sent = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        """
        Returns a human-readable string representation of the log entry.
        """
        return (f"{self.ip_address} - {self.request_method} "
                f"{self.request_uri} | {self.status_code}")
