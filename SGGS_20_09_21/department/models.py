from django.db import models

class department(models.Model):
    departmentname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.departmentname

class faculty(models.Model):
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    facultyname = models.CharField(max_length=100)
    facultyemail = models.EmailField(max_length=100)

    def __str__(self):
        return f"faculty name - {self.facultyname} , faculty_email - {self.facultyemail}"

class Students(models.Model):
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    noofsubjects = models.PositiveIntegerField(default=0)
    noofstudents = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Year - {self.year} , No of Students - {self.noofstudents} "





