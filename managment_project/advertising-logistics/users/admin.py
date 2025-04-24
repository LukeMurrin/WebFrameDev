from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'date_joined')  # Include the role field
    search_fields = ('username', 'email')
    list_filter = ('role', 'date_joined')

    def has_change_permission(self, request, obj=None):
        # Allow only admin users to make changes
        if request.user.is_superuser or getattr(request.user, 'role', None) == 'Admin':
            return True
        return super().has_change_permission(request, obj)