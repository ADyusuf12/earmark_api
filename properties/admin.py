from django.contrib import admin
from .models import Property, PropertyCategory
from accounts.models import UserProfile

class PropertyAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'owner_profile':
            kwargs["queryset"] = UserProfile.objects.filter(
                user__groups__name__in=['Owner', 'Agent', 'Developer']
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyCategory)
