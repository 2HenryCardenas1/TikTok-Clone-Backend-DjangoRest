from rest_framework.serializers import ModelSerializer

from users.api.serializers import UserSerializer
from video.models import Video


class VideoSerializer (ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'description', 'video', 'image', 'user', 'user_data',
                  'share_counter', 'likes_counter', 'created_at')
