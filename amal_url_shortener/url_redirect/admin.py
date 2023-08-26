from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
from .models import Url

class UrlsAdmin(admin.ModelAdmin):
    fields = ['url', 'url_short','visits','user','pub_date',]
    list_display = ('url', 'url_short','visits', 'user','pub_date',)

admin.site.register(Url, UrlsAdmin)

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('premium',)}),
    )

admin.site.register(User, UserAdmin)