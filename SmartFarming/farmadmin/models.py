from django.db import models
category=[
    ('tool','Machinery'),
    ('pesticide','Pesticide')
]
class login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    keyuser=models.CharField(max_length=20)

class customerdetails(models.Model):
    cname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phoneno=models.BigIntegerField(max_length=100)
    address=models.TextField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.cname

class customerproductorder(models.Model):
    customer_id=models.ForeignKey('customerdetails',on_delete=models.CASCADE)
    product=models.ForeignKey("farmer.addProduct",on_delete=models.CASCADE)
    quantity=models.IntegerField()
    address=models.TextField(max_length=100)
    contactno=models.BigIntegerField(max_length=100)
    status=models.CharField(max_length=50,default='pending') 

class customermachineryorder(models.Model):
    customer_id=models.ForeignKey('customerdetails',on_delete=models.CASCADE)
    product=models.ForeignKey("seller.sellingProducts",on_delete=models.CASCADE)
    pcategory=models.CharField(max_length=50,choices=category,default='tool')
    quantity=models.FloatField(max_length=100)
    address=models.TextField(max_length=100)
    contactno=models.BigIntegerField(max_length=100)
    status=models.CharField(max_length=100,default='pending')

