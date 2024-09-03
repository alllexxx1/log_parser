from rest_framework.routers import DefaultRouter

from log_parser.logs.views import LogEntryViewSet


router = DefaultRouter()
router.register(r'logs', LogEntryViewSet)

urlpatterns = router.urls
