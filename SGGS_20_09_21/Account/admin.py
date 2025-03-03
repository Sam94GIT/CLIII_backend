from django.contrib import admin
from .models import Studentprofile,Academics,Fees,HostelAndMess

class Studentprofileadmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name','regno','year','email','scholarshipname']
    search_fields = ['name','regno','year']

admin.site.register(Studentprofile,Studentprofileadmin)

class Academicsadmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['semester','currentbacklogs','cgpa']
    search_fields = ['semester','currentbacklogs','cgpa']

admin.site.register(Academics,Academicsadmin)


class Feesadmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['feespaid','feesremaining']
    search_fields = ['feespaid','feesremaining']

admin.site.register(Fees,Feesadmin)

class HostelAndMessadmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['Hostelname','Hostelfeespaid','messfeespaid']
    search_fields = ['Hostelname','Hostelfeespaid','messfesspaid']

admin.site.register(HostelAndMess,HostelAndMessadmin)






