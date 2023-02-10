from datetime import datetime


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.

class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    name = models.CharField(max_length=250,null=True)
    phonenumber = models.IntegerField(null=True)
    DOB = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='photo',null=True,blank=True)

    def age(self):
        today = timezone.now().date()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age



class addmarks(models.Model):
    student=models.ForeignKey(Login,on_delete=models.CASCADE)
    marks=models.IntegerField()

