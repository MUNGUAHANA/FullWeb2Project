''' from django.db import models
# Create your models here.
class Les_produits(models.Model):
    name = models.CharField(unique=True, max_length=100)
    Details = models.TextField(blank=True)
    Quantity= models.IntegerField(default=0)
    Unit_Price= models.IntegerField(default=0)
    Total_price= models.IntegerField(default=0)
  
class achat (models.Model):
    customer = models.CharField(unique=True, max_length=100)
    date = models.DateField(null=True, blank=True)
    product = models.ForeignKey (Les_produits, to_field='name', on_delete=models.CASCADE)
    quantityBuy= models.IntegerField(default=0)
    money= models.IntegerField(default=0)
    confirm = models.BooleanField(default=True)
    
    
class se_connecter (models.Model):
    password = models.CharField(primary_key=True, unique=True,max_length=10)
    User_name = models.CharField(unique=True, max_length=100)
    Adress_of_the_User = models.TextField(blank=False)
    
     '''