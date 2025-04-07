from django.db import models

# Create your models here.

class Author(models.Model):
    authorname = models.CharField(max_length=200)

    def __str__(self):
        return self.authorname

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publicationdate = models.DateField()
    # book_id = models.AutoField(primary_key=True)  # AutoField is the default primary key

    def __str__(self):
        return f'{self.title} by {self.author}'


class Student(models.Model):
    Studentname = models.CharField(max_length=200)
    emailid = models.EmailField(max_length=254)
    borrowlimit = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.Studentname

class BorrowingTransaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowdate = models.DateField()
    returndate = models.DateField()





