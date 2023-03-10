from django.db import models

# Create your models here.
class job(models.Model):
    title=models.varchar(225)
    position=models.varchar(225)
    category=models.varchar(225)
    location=models.varchar(225)
    description=models.varchar(225)
    userld=models.int()
    salary=models.varchar(225)
class resume(models.Model):
    title=models.varchar(225)
    name=models.varchar(225)
    email=models.varchar(225)
    address=models.varchar(225)
    phone no=models.varchar(225)
    experiance=models.varchar(225)
    


    

    