from django.contrib import admin
from .models import Order

# Register the Order model in the admin interface
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'parcel', 'order_date')
    # Fields to search in the admin interface
    search_fields = ('user__username', 'parcel__tracking_number')
    # Filters to apply in the admin interface
    list_filter = ('order_date',)
