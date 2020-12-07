from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, Permission, User

from malsearch.models import Sample, ScanResult


class CustomAdminSite(AdminSite):
    site_header = "MalSearch Admin"


admin_site = CustomAdminSite(name="myadmin")
# Register your models here.
admin_site.register(User)
admin_site.register(Permission)
admin_site.register(Group)

admin_site.register(Sample)
admin_site.register(ScanResult)
