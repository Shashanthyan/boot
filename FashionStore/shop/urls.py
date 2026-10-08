from django.urls import path
from shop import views
from .views import ProductAPI

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Product listing
    path('product/', views.product, name='product'),
    # Product detail
    path('productdet/<int:pk>/', views.producto, name='productsdet'),

    # path('cart/', views.cart, name='cart'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('wishlist/', views.wishlist, name='wishlist'),

    # Category
    path('category/<str:category_name>/', views.category, name='category'),
    #search
    path('search/', views.search, name='search'),

    path("product/", ProductAPI.as_view()),    # GET all / POST
    path("products/<int:id>/", ProductAPI.as_view()),   # GET one / PUT / DELETE



]