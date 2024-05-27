from django.urls import path
from . import views

app_name="pages"
urlpatterns = [
    path('', views.home,name='home'), 
    path('product/', views.product, name='product'), 
    path('users/', views.users, name='users'), 
    path('add/',views.addNewProduct, name='addNewProduct'),
    path('buy/',views.buyProduct, name='buyProduct'),
    path('post/<int:post_id>/change/', views.update, name='update'),
    path('post/<int:post_id>/delete/', views.deleteArticle, name='deleteArticle'),
    path('post/<int:post_id>/', views.utilisateurs,name='utilisateurs'), 
    path('wishlist/', views.wishlist, name='wishlist'),
]
