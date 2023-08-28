from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Courses(models.Model):
    courseName = models.CharField(max_length=100, primary_key=True)
    courseFee = models.IntegerField()
    courseDuration = models.IntegerField()
    syallbus = RichTextField(default="syallbus")
    About_Course = RichTextField(default="About course")
    stars = models.IntegerField(default=3)
    images = models.ImageField(upload_to="course", null=True, blank=True)
    
    def __str__(self):
        return self.courseName
    
class Trainer(models.Model):
    trainer_name = models.CharField(max_length=100)
    trainer_designation = models.CharField( max_length=150)
    trainer_experience = models.DecimalField( max_digits=5, decimal_places=2)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.trainer_name
    
class Registration(models.Model):
    condidateId=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    father_name=models.CharField(max_length=40)
    phoneNumber=models.CharField(max_length=12)
    alternetPhoneNumber=models.CharField(max_length=12)
    email = models.EmailField()
    collegename=models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pincode = models.IntegerField()
    qualifaction = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)
    trainer = models.ForeignKey(Trainer,on_delete=models.DO_NOTHING,null=True)
    
    def __str__(self):
        return self.fname
    
class Payment(models.Model):
    name = models.ForeignKey(Registration,on_delete=models.SET_NULL,null=True)
    fee=models.IntegerField()
    balance = models.IntegerField()
    status = models.CharField(default='Unpaid',max_length=20)
    
    


class Attendance(models.Model):
    student = models.ForeignKey(Registration, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.fname} on {self.date}: {'Present' if self.present else 'Absent'}"

    
    
    