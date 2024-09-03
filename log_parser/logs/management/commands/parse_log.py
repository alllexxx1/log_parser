import json
from datetime import datetime

from django.core.management.base import BaseCommand

from log_parser.logs.models import LogEntry


class Command(BaseCommand):
    """
    Custom management command to process and aggregate Nginx log data into the database.

    Defining this class enables using 'parse_log' as a manage.py command.
    """

    help = ('Process and aggregate essential '
            'Nginx log files information into the database')

    def add_arguments(self, parser):
        """
        Adds arguments that the command 'parse_log' accept

        - `logfile_path`: The file path of the Nginx log file to be processed.
        """
        parser.add_argument('logfile_path', type=str, help='Path to the Nginx log file')

    def handle(self, *args, **kwargs):
        """
        The main logic of the command.

        - Reads the specific log file line by line.
        - Parses essential data.
        - Creates and saves a LogEntry instance in a database.
        - Displays progress to the user.
        """

        # Since log files might be quite large and processing
        # may not be as fast as we want, we should notify the user
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
