from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from video.api.serializer import VideoSerializer
from video.models import Video


class VideoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer

    queryset = Video.objects.all()
    http_method_names = ['get', 'post']
    # Filtering
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # Filter by userId, the user who created the video
    filterset_fields = ['user']
    # Order by created_at
    ordering = ['-created_at']
