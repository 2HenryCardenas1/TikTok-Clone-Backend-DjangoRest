from comment.api.serializers import CommentSerializer
from comment.models import Comment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['video']
    ordering_fields = ['-created_at']
