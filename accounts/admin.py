from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, UserInterest

# Register UserInterest normally
admin.site.register(UserInterest)

# Inline UserProfile into User admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    filter_horizontal = ('interests',)  # Enables multi-select UI

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# Unregister default User admin and register custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
