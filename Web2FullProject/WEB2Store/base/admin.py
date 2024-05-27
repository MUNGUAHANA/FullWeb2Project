from django.contrib import admin
#from django.contrib.auth.models import Group,User,Permission,get_user_model
#from django.contrib.contenttypes.models import ContentType
#User=get_user_model()
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
# Register your models here.

from django.contrib import admin
# import the models
from .models import *
# register each model with the admin site
admin.site.register(Les_produits)
admin.site.register(achat)
admin.site.register(se_connecter)
 
''' can_add= Permission.objects.get(codename='Add_products') 
creators=can_add.user_set.all() '''
''' agents,created=Group.objects.get_or_create(name='agents')
agents.save()
Mariam=User.objects.get(username='Mariam')
agents.User_set.add(Mariam) '''

''' sellers = Group(name='sellers')
sellers.save()
sellers = Group.objects.get(name='Dave')
sellers = sellers.user_set.all()


Add_products = Permission.objects.get(codename='Add_products')
sellers.permissions.add(Add_products)  '''