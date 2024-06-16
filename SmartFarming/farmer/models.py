from django.db import models
usertype=[
    ('farmer','Farmer'),
    ('worker','Worker')
]

class farmerregister(models.Model):
    farmername=models.CharField(max_length=50)
    phoneno=models.BigIntegerField(max_length=50)
    address=models.TextField(max_length=100)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.farmername

class addProduct(models.Model):
    farmerregister_id=models.ForeignKey('farmerregister',on_delete=models.CASCADE)
    productname=models.CharField(max_length=50)
    productimage=models.ImageField()
    description=models.CharField(max_length=50,default="none")
    price=models.FloatField(max_length=50)
    status=models.CharField(max_length=50)
    def __str__(self):
        return self.productname
    
class sendJobRequest(models.Model):
    farmerregister_id=models.ForeignKey('farmerregister',on_delete=models.CASCADE)
    description=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    payperday=models.FloatField()
    workerid=models.ForeignKey("worker.workerregister",on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default='pending') 


class sendToolOrderRequest(models.Model):
    userid=models.BigIntegerField(max_length=50)
    usertype=models.CharField(max_length=50,choices=usertype,default='Farmer')
    toolid=models.ForeignKey("seller.sellingProducts",on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.CharField(max_length=50,default='pending') 

class sendRentRequest(models.Model):
    farmerregister_id=models.ForeignKey('farmerregister',on_delete=models.CASCADE)
    toolid=models.ForeignKey("seller.rentTools",on_delete=models.CASCADE)
    nooftools=models.IntegerField()
    duration=models.IntegerField()
    status=models.CharField(max_length=50,default='pending') 


