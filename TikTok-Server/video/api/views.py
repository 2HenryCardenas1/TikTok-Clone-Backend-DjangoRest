from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from video.api.serializer import (VideoActionsSerializer, VideoLikeSerializer,
                                  VideoSerializer)
from video.models import Video, VideoLike


class VideoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer

    queryset = Video.objects.all()
    http_method_names = ['get', 'post']
    # Indicator of libraries to use
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # Filter by userId, the user who created the video, endpoint /api/videos/?user=1
    filterset_fields = ['user']
    # Order by created_at
    ordering = ['-created_at']


class VideoActionsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoActionsSerializer

    queryset = Video.objects.all()
    http_method_names = ['put']


class VideoLikeApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoLikeSerializer

    queryset = VideoLike.objects.all()
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'video']
