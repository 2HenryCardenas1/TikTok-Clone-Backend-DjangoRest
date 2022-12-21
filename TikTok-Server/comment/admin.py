from comment.models import Comment
from django.contrib import admin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'video', 'created_at')
