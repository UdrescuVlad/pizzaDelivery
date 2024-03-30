from django.contrib import admin
from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(BillingProfile)
class BillingProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    pass