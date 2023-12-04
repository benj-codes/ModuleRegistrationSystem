from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import CourseGroup
from django.utils.translation import gettext_lazy as _
# Register your models here.

admin.site.unregister(Group)

@admin.register(CourseGroup)
class CourseGroupAdmin(GroupAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'permissions')}),
        (_('Description'), {'fields': ('description',)}),
    )