from django.contrib import admin
from .models import Book,Author,Student,BorrowingTransaction

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['authorname','authorid']
    search_fields = ['authorname']

admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['title','author','publicationdate','bookid']
    search_fields = ['title','bookid']

admin.site.register(Book,BookAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Studentname','Studentid','emailid','borrowlimit']
    search_fields = ['Studentname','Studentid']

admin.site.register(Student,StudentAdmin)

class BorrowTransactionAdmin(admin.ModelAdmin):
    list_display = ['student','book','borrowdate','returndate']

admin.site.register(BorrowingTransaction,BorrowTransactionAdmin)
