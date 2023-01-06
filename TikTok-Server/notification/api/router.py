from notification.api.views import NotificationApiViewSet
from rest_framework.routers import DefaultRouter

router_notification = DefaultRouter()

router_notification.register(prefix='notification',
                             viewset=NotificationApiViewSet, basename='notification')
