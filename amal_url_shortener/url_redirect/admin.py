from django.contrib import admin

# Register your models here.
from .models import Urls

class UrlsAdmin(admin.ModelAdmin):
    fields = ['url', 'url_short','visits','pub_date',]
    list_display = ('url', 'url_short','visits','pub_date',)

admin.site.register(Urls, UrlsAdmin)