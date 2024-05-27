from django import forms
from base.models import*
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Les_produits
        fields = [ 'name', 'Details', 'Quantity','Unit_Price','Total_price','image']
        
class buyForm(forms.ModelForm):
    class Meta:
        model = achat
        fields = [ 'customer', 'date', 'product','quantityBuy','money','image']
            
            
            
            
