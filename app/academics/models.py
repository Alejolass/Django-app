#Jairo
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    email=models.EmailField(null= True, blank = True)
    password= models.CharField(null= True, blank = True)
    status= models.BooleanField(null= True, blank = True)
    cre_at=models.DateTimeField(default=datetime.datetime.now())
    updated_at=models.DateTimeField(default=datetime.datetime.now())
    deleted_at= models.DateTimeField(null= True, blank = True)

class Person(models.Model):
     firstname = models.CharField(max_length=20)
     lastname=models.CharField(max_length=20)
     id_ident_type = models.IntegerField(null=False), models.ForeignKey('identification_types',on_delete=models.CASCADE)
     age = models.IntegerField()
     ident_number=models.CharField(max_length=12, blank=True)
     id_exp_city = models.IntegerField(null=False), models.ForeignKey('cities',on_delete=models.CASCADE)
    
     
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)










