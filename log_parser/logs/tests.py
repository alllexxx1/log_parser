from django.test import TestCase
from log_parser.logs.models import LogEntry
from django.core.management import call_command


class LogsProcessingTestCase(TestCase):
    def test_parse_log_command(self):
        call_command(
            'parse_log',
            './log_parser/logs/test_data/nginx_logs.txt'
        )
        self.assertEqual(LogEntry.objects.count(), 5)

    def test_log_entry_api(self):
        response = self.client.get('/api/logs/')
        self.assertEqual(response.status_code, 200)

    def test_filter_parameters_api(self):
        response = self.client.get('/api/logs/?status_code=304')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_swagger(self):
        response = self.client.get('/swagger')
        self.assertEqual(response.status_code, 301)
