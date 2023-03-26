from django.contrib import admin
from .models import Profile,Job,Resume,Application, Category


class ProfileAdmin(admin.ModelAdmin):
    list_filter =("id","user_type")
    list_display =("id","user_type")

admin.site.register(Profile,ProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_filter =("id","name")
    list_display =("id","name")

admin.site.register(Category,CategoryAdmin)

class JobAdmin(admin.ModelAdmin):
    list_filter =("id","title","position")
    list_display =("id","title","position")


admin.site.register(Job, JobAdmin)

class ResumeAdmin(admin.ModelAdmin):
    list_filter =("id","title","name")
    list_display =("id","title","name")


admin.site.register(Resume,ResumeAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_filter =("id","applied_by")
    list_display =("id","applied_by")

admin.site.register(Application,ApplicationAdmin)