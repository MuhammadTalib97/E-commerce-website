from django.db import models

# Create your models here.
class seller(models.Model):
    name=models.CharField(max_length=60)
    uname=models.CharField(max_length=40)
    email=models.EmailField()
    phoneno=models.CharField(max_length=50,blank=True,default=None)
    bankname=models.CharField(max_length=50,blank=True,default=None)
    ifsccode=models.CharField(max_length=20,blank=True,default=None)
    accountnumber=models.CharField(max_length=25,blank=True,default=None)
    total=models.IntegerField(blank=True,default=None,null=True)
    def __str__(self):
        return str(self.id)+' '+self.name

class category(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return str(self.id)+' '+self.name

class brand(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return str(self.id)+' '+self.name

class product(models.Model):
    stock=models.BooleanField(default=False)
    name=models.CharField(max_length=30)
    desc=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    seller=models.ForeignKey(seller,on_delete=models.CASCADE)
    baseprice=models.IntegerField()
    discount=models.IntegerField(default=0,null=True,blank=True)
    finalprice=models.FloatField(default=0,null=True,blank=True)
    red=models.BooleanField(default=False,null=True,blank=True)
    green=models.BooleanField(default=False,null=True,blank=True)
    white=models.BooleanField(default=False,null=True,blank=True)
    pink=models.BooleanField(default=False,null=True,blank=True)
    xs=models.BooleanField(default=False,null=True,blank=True)
    s=models.BooleanField(default=False,null=True,blank=True)
    m=models.BooleanField(default=False,null=True,blank=True)
    l=models.BooleanField(default=False,null=True,blank=True)
    xl=models.BooleanField(default=False,null=True,blank=True)
    xxl=models.BooleanField(default=False,null=True,blank=True)
    img1=models.ImageField(upload_to='images/',default=None,blank=True)
    img2=models.ImageField(upload_to='images/',default=None,blank=True)
    img3=models.ImageField(upload_to='images/',default=None,blank=True)
    img4=models.ImageField(upload_to='images/',default=None,blank=True)
    img5=models.ImageField(upload_to='images/',default=None,blank=True)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.id)+' '+ self.name

class buyer(models.Model):
    name=models.CharField(max_length=30)
    uname=models.CharField(max_length=34)
    email=models.EmailField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=20,default=None,blank=True)
    address1=models.CharField(max_length=30,default=None,blank=True)
    address2=models.CharField(max_length=30,default=None,blank=True)
    city=models.CharField(max_length=30,default=None,blank=True)
    state=models.CharField(max_length=30,default=None,blank=True)
    pin=models.CharField(max_length=30,default=None,blank=True)
    def __str__(self):
        return str(self.id)+' '+self.name

class cart(models.Model):
    buyer=models.ForeignKey(buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    color=models.CharField(max_length=40,default=None)
    size=models.CharField(max_length=30,default=None)
    def __str__(self):
        return str(self.id)+" "+self.buyer.name
class checkout(models.Model):
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    address=models.CharField(max_length=30)
    name=models.CharField(max_length=40,default=None)
    email=models.EmailField(default=None,blank=True)
    address2=models.CharField(max_length=50)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=20)
    pin=models.CharField(max_length=50)
    note=models.TextField()
    mode=models.CharField(max_length=40,default=None)
    def __str__(self):
        return str(self.id)
class wishlist(models.Model):
    user=models.ForeignKey(buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    subject=models.CharField(max_length=40) 
    msg=models.TextField()
    def __str__(self):
        return str(self.id)+" "+self.name               