from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)  # Register your model with the admin site
class ProfileAdmin(admin.ModelAdmin):
    pass  # Use the default admin interface