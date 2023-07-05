from django.contrib import admin
from .models import College,News,Events,department,Partners,HelpTexts,Univesity,Facilities,Office,Staffmember,Gallery, Programs, Departmentfacilities
admin.site.register(College)
admin.site.register(News)
admin.site.register(Events)
admin.site.register(department)
admin.site.register(Partners)
admin.site.register(HelpTexts)

admin.site.register(Facilities)

admin.site.register(Staffmember)
admin.site.register(Gallery)
admin.site.register(Programs)
admin.site.register(Departmentfacilities)


class OfficeAdmin(admin.ModelAdmin):
   
   
   def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Office, OfficeAdmin)
class UniversityAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
         if Univesity.objects.exists():
             return False
         else:
             return True

admin.site.register(Univesity, UniversityAdmin)