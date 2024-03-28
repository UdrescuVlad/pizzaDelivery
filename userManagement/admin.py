from django.contrib import admin
from .models import Profile

@admin.register(Profile)  # Register your model with the admin site
class ProfileAdmin(admin.ModelAdmin):
    pass  # Use the default admin interface