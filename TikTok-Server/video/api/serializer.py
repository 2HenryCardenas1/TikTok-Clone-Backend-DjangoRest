from follow.models import Follow
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from users.api.serializers import UserSerializer
from video.models import Video, VideoLike


class VideoSerializer (ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'description', 'video', 'image', 'user', 'user_data',
                  'share_counter', 'likes_counter', 'created_at')


class VideoActionsSerializer (ModelSerializer):
    class Meta:
        model = Video
        fields = ('likes_counter', 'share_counter')


class VideoLikeSerializer (ModelSerializer):
    video_data = VideoSerializer(source='video', read_only=True)

    class Meta:
        model = VideoLike
        fields = ('id', 'user', 'video', 'video_data', 'created_at')


class VideoNotificationSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'image']
