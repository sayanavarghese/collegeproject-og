from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
        CHOICES = (
        ("ADMIN", "ADMIN"),
        ("JOB_ADDER", "JOB_ADDER"),
        ("USER", "USER"),
)
        user =models.OneToOneField(User, on_delete= models.CASCADE)
        user_type =models.CharField(max_length=150, choices =CHOICES, default ='USER')

class Category(models.Model):
      name = models.CharField(max_length=255)

      def __str__(self):
        return self.name


class Job(models.Model):
    title=models.CharField(max_length=225)
    position=models.CharField(max_length=225)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    location=models.TextField()
    description=models.TextField()
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)
    salary=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    
class Resume(models.Model):
    title=models.CharField(max_length=225)
    name=models.CharField(max_length=225)
    email=models.EmailField(max_length=225)
    address=models.TextField()
    experiance=models.TextField()
    qualification=models.TextField()
    phone_no=models.CharField(max_length=12)
    about_me=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Application(models.Model):
        applied_by=models.ForeignKey(User,on_delete=models.CASCADE)
        job=models.ForeignKey(Job,on_delete=models.CASCADE)
       


    

    