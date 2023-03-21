from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_filter =("id","user_type")
    list_display =("id","user_type")

admin.site.register(Profile,ProfileAdmin)