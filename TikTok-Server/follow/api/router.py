from django.urls import path
from follow.api.views import (FollowApiVewSet, FollowedCountView,
                              FollowersCountView)
from rest_framework.routers import DefaultRouter

router_follow = DefaultRouter()
router_follow.register(
    prefix='follow', basename='follow', viewset=FollowApiVewSet)

urlpatterns = [
    path('follow/followed/count/<int:id_user>', FollowedCountView.as_view()),
    path('follow/followers/count/<int:id_user>', FollowersCountView.as_view()),

]
