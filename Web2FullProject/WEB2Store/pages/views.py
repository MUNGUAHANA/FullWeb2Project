from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404
from WEB2Store.forms import BlogPostForm, buyForm
from django.contrib.auth.decorators import permission_required
from base.models import*
from django.db.models.signals import post_save 
from django.dispatch import receiver

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
def product(request):
    posts=Les_produits.objects.all()
    data={
        'Les_produits':posts
    }
    if request.method == 'POST': 
        if request.user.is_authenticated: 
            WishlistItem.objects.get_or_create( user=request.product, product=product ) 
            data['wishlist_message'] = 'Product added to wishlist!' 
        else: data['wishlist_message'] = 'Please login to add to wishlist.' 
    return render(request, 'pages/products.html', data)

def wishlist(request): 
    user = request.product 
    wishlist_items = WishlistItem.objects.filter(user=user).select_related('product') 
    context = {'wishlist_items': wishlist_items}
    return render(request, 'wishlist.html', context)

def users(request):
    return render(request, 'pages/users.html')

def utilisateurs(request, post_id):
    try:
       blog_post=se_connecter.objects.get(id=post_id)
    except :
        raise Http404('This user does not exist yet')
    
    data1={'post':blog_post}
    return render(request, 'pages/utilisateurs.html', data1)

#@permission_required('blog.add_products', raise_exception=True)
def addNewProduct(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product/')
    else:
        form = BlogPostForm()
    return render(request, 'pages/add_product.html', { 'form': form })


def buyProduct(request):
    if request.method == "POST":
        form = buyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'pages/success.html')
    else:
        form = buyForm()
    return render(request, 'pages/buy.html', { 'form': form })

def update(request, post_id):
    post = get_object_or_404(Les_produits, id=post_id) 
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save() 
            return redirect('/product/')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'pages/edit.html', { 'form': form, 'post': post })

def deleteArticle(request, post_id):
    post = get_object_or_404(Les_produits, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('/product/')
    return render(request, 'pages/Productdelete.html', { 'post': post })


@receiver(post_save, sender=Les_produits) 
def create_notification(sender, instance, created, **kwargs): 
    if created: # Create a notification when a new product is saved
        Notification.objects.create( message=f"New product added: {instance.name}", ) 
       
''' def incementFunct(Les_produits,Quantity,post_id, increment=True):
    instance=get_object_or_404(Les_produits,id=post_id)
    setattr(instance, Quantity, getattr(instance, Quantity) +(1 if increment))  '''   
'''def wishlist(request): 
    user = request.user 
    wishlist_items = WishlistItem.objects.filter(user=user).select_related('product') 
    context = {'wishlist_items': wishlist_items}
    
    return render(request, 'wishlist.html', context)'''

