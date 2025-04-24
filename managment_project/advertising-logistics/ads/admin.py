from django.contrib import admin
from .models import Ad

# Admin configuration for the Ad model
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'revenue')  # Fields to display in the admin list view
    search_fields = ('title',)  # Enable search by title
    list_filter = ('is_active',)  # Add a filter for active/inactive ads
