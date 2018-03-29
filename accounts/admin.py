from django.contrib import admin
from accounts.models import UserProfile
#from accounts import models

# Register your models here.
admin.site.register(UserProfile)


"""
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='Manipal')
"""

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    user_info.short_description = 'Info'

    def get_queryset(self, request):
        queryset= super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('phone')
        return queryset


admin.site.unregister(UserProfile)
admin.site.register(UserProfile, UserProfileAdmin)
