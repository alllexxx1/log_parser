import json
from datetime import datetime

from django.core.management.base import BaseCommand

from log_parser.logs.models import LogEntry


class Command(BaseCommand):
    help = ('Process and aggregate essential '
            'Nginx log files information into the database')

    def add_arguments(self, parser):
        parser.add_argument('logfile_path', type=str, help='Path to the Nginx log file')

    def handle(self, *args, **kwargs):
        self.stdout.write('Bare with me, it might take some time')

        logfile_path = kwargs['logfile_path']
        with open(logfile_path, 'r') as logfile:
            for line in logfile:
                log_data = json.loads(line.strip())

                request_part = log_data['request'].split()
                method = request_part[0]
                uri = request_part[1]

                log_entry = LogEntry(
                    date=datetime.strptime(
                        log_data['time'],
                        '%d/%b/%Y:%H:%M:%S %z'
                    ),
                    ip_address=log_data['remote_ip'],
                    request_method=method,
                    request_uri=uri,
                    status_code=int(log_data['response']),
                    bytes_sent=int(log_data['bytes']),
                )
                log_entry.save()

        self.stdout.write(
            self.style.SUCCESS(
                'Log file processed, data saved in data base'
            )
        )
