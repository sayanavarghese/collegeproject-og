from django.db import models

# Create your models here.
class job(models.Model):
    title=models.TextField(max_length=225)
    position=models.TextField(max_length=225)
    category=models.TextField(max_length=225)
    location=models.TextField(max_length=225)
    description=models.TextField(max_length=225)
    userld=models.IntegerField()
    salary=models.TextField(max_length=225)
class resume(models.Model):
    title=models.TextField(max_length=225)
    name=models.TextField(max_length=225)
    email=models.EmailField(max_length=225)
    address=models.TextField(max_length=225)
    experiance=models.TextField(max_length=225)
    


    

    