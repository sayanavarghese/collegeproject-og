from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class job(models.Model):
#     title=models.TextField(max_length=225)
#     position=models.TextField(max_length=225)
#     category=models.TextField(max_length=225)
#     location=models.TextField(max_length=225)
#     description=models.TextField(max_length=225)
#     userld=models.IntegerField()
#     salary=models.TextField(max_length=225)
# class resume(models.Model):
#     title=models.TextField(max_length=225)
#     name=models.TextField(max_length=225)
#     email=models.EmailField(max_length=225)
#     address=models.TextField(max_length=225)
#     experiance=models.TextField(max_length=225)
class Profile(models.Model):
        CHOICES = (
        ("ADMIN", "ADMIN"),
        ("JOB_ADDER", "JOB_ADDER"),
        ("USER", "USER"),
)
        user =models.OneToOneField(User, on_delete= models.CASCADE)
        user_type =models.CharField(max_length=150, choices =CHOICES, default ='USER')



    

    