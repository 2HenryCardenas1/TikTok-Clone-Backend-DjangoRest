from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User

# Register your models here to saw in the web.

# This a decorator (@admin.register(User)) is indicator to use model User.


@admin.register(User)
# This class extends the default model django UserAdmin class
# but we change the parameters the this a model.
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_superuser',
                    'is_staff', 'date_joined']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
         'last_name', 'email', 'description', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Social Networks'), {'fields': ('instagram', 'website')}),
    )

    readonly_fields = ['date_joined', 'last_login']
