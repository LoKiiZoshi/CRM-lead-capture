# Admin configuration for leads
from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    # Customize admin interface for leads
    list_display = ('email', 'first_name', 'last_name', 'source', 'created_at')  # Columns to display
    list_filter = ('source', 'created_at')  # Filters for admin
    search_fields = ('email', 'first_name', 'last_name', 'company')  # Searchable fields
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing timestamps