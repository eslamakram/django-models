from django.contrib import admin
from .models import Snack

# Register your models here.

# class AdminSnack(admin.ModelAdmin):
#       list_display = ['name', 'description']
#       search_fields = ['name']
#       list_display_links = ['purcheser']

admin.site.register(Snack)