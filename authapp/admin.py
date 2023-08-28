from django.contrib import admin
from .models import *

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display = ('name','Email', 'phone')
admin.site.register(Contact, contactAdmin)