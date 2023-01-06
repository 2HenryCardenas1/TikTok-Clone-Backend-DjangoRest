from django.db import models

NotificationTypeEnum = (
    ('FOLLOW', 'follow'),
    ('LIKE', 'like'),
    ('COMMENT', 'comment'),
    ('SHARE', 'share')
)
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='notifications_user')
    user_follower = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='notifications_user_follower')
    video = models.ForeignKey(
        'video.Video', on_delete=models.CASCADE, null=True, blank=True)
    type_notification = models.CharField(
        max_length=255, choices=NotificationTypeEnum)
    comment = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
