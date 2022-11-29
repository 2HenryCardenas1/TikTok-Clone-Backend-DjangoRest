from django.contrib import admin

from video.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'video', 'image', 'user',
                    'share_counter', 'likes_counter', 'created_at')
