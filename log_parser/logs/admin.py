from django.contrib import admin

from log_parser.logs.models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        'ip_address',
        'request_method',
        'request_uri',
        'status_code',
        'bytes_sent',
        'date',
    )
    list_filter = ('request_method', 'status_code', 'date')
    search_fields = ('ip_address', 'request_uri')


admin.site.site_title = 'NGINX logs admin-panel'
admin.site.site_header = 'NGINX logs admin-panel'
