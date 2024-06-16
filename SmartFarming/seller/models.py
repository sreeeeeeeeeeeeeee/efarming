from django.db import models
usertype=[
    ('seller','Seller'),
    ('worker','Worker')
]

class sellerregister(models.Model):
    ownername=models.CharField(max_length=50)
    phoneno=models.BigIntegerField()
    address=models.TextField(max_length=50)
    shopname=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.IntegerField(default=0)

class sellingProducts(models.Model):
    sellerregister_id=models.ForeignKey('sellerregister',on_delete=models.CASCADE)
    pname=models.CharField(max_length=50)
    pimage=models.ImageField()
    pcategory=models.CharField(max_length=20)
    description=models.CharField(max_length=50,default="none")
    price=models.FloatField(max_length=50)
    status=models.CharField(max_length=50)
    def __str__(self):
        return self.pname

class rentTools(models.Model):
    sellerregister_id=models.ForeignKey('sellerregister',on_delete=models.CASCADE)
    tname=models.CharField(max_length=50)
    timage=models.ImageField()
    description=models.CharField(max_length=50,default="none")
    priceperday=models.FloatField(max_length=50)
    nooftools=models.IntegerField(max_length=50)
    status=models.CharField(max_length=50)
    def __str__(self):
        return self.tname
    
class sendproductRequest(models.Model):
    userid=models.BigIntegerField(max_length=50)
    usertype=models.CharField(max_length=50,choices=usertype,default='Seller')
    product=models.ForeignKey("farmer.addProduct",on_delete=models.CASCADE)
    quantity=models.IntegerField()
    phoneno=models.BigIntegerField()
    status=models.CharField(max_length=50,default='pending') 