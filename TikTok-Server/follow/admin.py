from django.contrib import admin
from follow.models import Follow


# Register your models here.
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_followed', 'created_at')
