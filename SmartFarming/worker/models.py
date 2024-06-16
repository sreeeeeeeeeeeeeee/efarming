from django.db import models
class workerregister(models.Model):
    workername=models.CharField(max_length=50)
    age=models.IntegerField(max_length=50)
    gender=models.CharField(max_length=20)
    phoneno=models.BigIntegerField(max_length=50)
    address=models.TextField(max_length=50)
    occupation=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.workername
    
    
# Create your models here.
