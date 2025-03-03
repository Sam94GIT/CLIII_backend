from django.db import models

class Studentprofile(models.Model):
    name = models.CharField(max_length=30)
    regno = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    year = models.CharField(max_length=10)
    scholarshipname = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.regno} - {self.year}"

class Academics(models.Model):
    student = models.ForeignKey(Studentprofile, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    currentbacklogs = models.PositiveIntegerField(default=0)
    cgpa = models.FloatField(default=0.0)

    def __str__(self):
        return self.semester

class Fees(models.Model):
    student = models.ForeignKey(Studentprofile, on_delete=models.CASCADE)
    feespaid = models.BooleanField(default=True)
    feesremaining = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f" fess paid - {self.feespaid}"

class HostelAndMess(models.Model):
    student = models.ForeignKey(Studentprofile, on_delete=models.CASCADE)
    Hostelname = models.CharField(max_length=10)
    Hostelfeespaid = models.BooleanField(default=True)
    messfeespaid = models.BooleanField(default=True)


    def __str__(self):
        return f" Hostel name - {self.Hostelname}"



