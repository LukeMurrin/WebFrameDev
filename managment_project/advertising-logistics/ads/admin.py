from django.contrib import admin
from .models import Ad

# Register the Ad model in the admin interface
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'is_active', 'revenue')
    # Fields to search in the admin interface
    search_fields = ('title',)
    # Filters to apply in the admin interface
    list_filter = ('is_active',)

    def has_change_permission(self, request, obj=None):
        # Allow only Admin and Advertiser to make changes
        if request.user.role in ['Admin', 'Advertiser']:
            return True
        return super().has_change_permission(request, obj)
