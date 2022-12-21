from comment.api.views import CommentApiViewSet
from rest_framework.routers import DefaultRouter

router_comment = DefaultRouter()

router_comment.register(prefix='comment', viewset=CommentApiViewSet,
                        basename='comment')
