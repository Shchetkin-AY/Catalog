from django.contrib import admin

# Register your models here.

from professions.models import Direction, Profile

class DirectionAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass




admin.site.register(Direction, DirectionAdmin)
admin.site.register(Profile, ProfileAdmin)