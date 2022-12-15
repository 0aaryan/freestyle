from django.contrib import admin, auth
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from shopping import views
from shopping.forms import Loginform
urlpatterns = [
    path('', views.index2, name='index'),
    path('home/', views.index2, name='home'),
    path('home/<category>', views.index1, name='home'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=Loginform), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path("products/<int:product_id>/", views.product, name="product"),
    path('cart/', views.cartView, name='cart'),
    path('addtocart/<int:product_id>/',views.addtocart,name='addtocart'),
    path('removefromcart/<int:product_id>/',views.removefromcart,name='removefromcart'),
    path('addprofile/',views.addProfile.as_view(),name='addprofile'),
    path('editprofile/',views.editProfile.as_view(),name='editprofile'),
    path('checkout/',views.checkout,name='checkout'),
]