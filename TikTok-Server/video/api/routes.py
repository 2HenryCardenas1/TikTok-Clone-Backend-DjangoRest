from rest_framework.routers import DefaultRouter
from video.api.views import (VideoActionsApiViewSet, VideoApiViewSet,
                             VideoLikeApiViewSet)

router_video = DefaultRouter()

router_video.register(prefix='video', basename='video',
                      viewset=VideoApiViewSet)


router_video.register(prefix='video/actions', basename='video',
                      viewset=VideoActionsApiViewSet)


router_video.register(prefix='video_like', basename='video',
                      viewset=VideoLikeApiViewSet)
