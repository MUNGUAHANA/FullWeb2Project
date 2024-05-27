from django.db import models
# Create your models here.

class Les_produits(models.Model):
    permissions = [
        ("Add_products", "Can add a product")
]
    name = models.CharField(unique=True, max_length=100)
    Details = models.TextField(blank=True)
    Quantity= models.IntegerField(default=0)
    Unit_Price= models.IntegerField(default=0)
    Total_price= models.IntegerField(default=0)
    image = models.ImageField(upload_to="pages\static\pages\img", null=True, blank=True)
    
    def __str__(self):
        return self.name
 
 
class WishlistItem(models.Model):
    product = models.ForeignKey(Les_produits, to_field='name', on_delete=models.CASCADE) 
    added_date = models.DateTimeField(auto_now_add=True) 

 
class achat (models.Model):
    customer = models.CharField(unique=False, max_length=100)
    date = models.DateField(null=True, blank=False, auto_now_add=False)
    product = models.ForeignKey (Les_produits, to_field='name', on_delete=models.CASCADE)
    quantityBuy= models.IntegerField(default=0)
    money= models.IntegerField(default=0)
    image = models.ImageField(upload_to="pages\static\pages\img", null=True, blank=True)
    confirm = models.BooleanField(default=True)
    
    def __str__(self):
        return self.customer
    
class se_connecter (models.Model):
    password = models.CharField(primary_key=True, unique=True,max_length=10)
    User_name = models.CharField(unique=True, max_length=100)
    Adress_of_the_User = models.TextField(blank=False)
    
    def __str__(self):
        return self.password
    

class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True) 
    message = models.CharField(max_length=255) 
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # Optional: Associate with user 
    
    def __str__(self): return f"{self.message} - {self.created}" 
    