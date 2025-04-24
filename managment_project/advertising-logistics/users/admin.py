from django.contrib import admin
from .models import User

# Register the User model in the admin interface
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Display basic user information
    list_display = ('username', 'email', 'role', 'date_joined')  # Display role
    # Allow searching by username and email
    search_fields = ('username', 'email')
    # Add role to filters
    list_filter = ('role', 'date_joined')

    def has_change_permission(self, request, obj=None):
        # Allow only admin users to make changes
        if request.user.role == 'Admin':
            return True
        return super().has_change_permission(request, obj)