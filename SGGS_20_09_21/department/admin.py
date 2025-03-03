from django.contrib import admin
from .models import department , faculty , Students

class departmentadmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['departmentname']
    search_fields = ['departmentname']

admin.site.register(department,departmentadmin)

class facultyadmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['facultyname','facultyemail']
    search_fields = ['facultyname']

admin.site.register(faculty,facultyadmin)

class studentadmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['year', 'noofstudents','noofsubjects']
    search_fields = ['year']

admin.site.register(Students,studentadmin)






