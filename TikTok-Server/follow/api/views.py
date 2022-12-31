from django_filters.rest_framework import DjangoFilterBackend
from follow.api.serializer import FollowSerializer
from follow.models import Follow
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class FollowApiVewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'user_followed']


class FollowedCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id_user = kwargs['id_user']
        followed_count = Follow.objects.filter(user=id_user).count()
        return Response({'followed_count': followed_count})


class FollowersCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id_user = kwargs['id_user']
        followers_count = Follow.objects.filter(user_followed=id_user).count()
        return Response({'followers_count': followers_count})
