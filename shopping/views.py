from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistration, Loginform,detailsform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from django.views.decorators.cache import cache_control
# Create your views here.

def index1(request,category):
    if category=="all" or category==None:
        products= models.product.objects.all()
    else:
        products= models.product.objects.filter(product_category__name=category)
    n1= len(products)
    allCat= models.category.objects.all()
    n2= len(allCat)
    params={'param1':{'range':range(1,n1), 'product': products},
            'param2':{'range':range(1,n2), 'category': allCat}}
    params['nav_links'] = True

    if request.user.is_authenticated:
        cart_user= request.user
        cart_items= models.cart.objects.filter(user=cart_user)
        params['num_of_cart_items']=len(cart_items)
    else:
        params['cart_items']=0
    return render(request, 'home.html',params)

def index2(request):
    return redirect('home',category="all")


class register(View):
    def get(self,request):
        form = CustomerRegistration()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations!! registered successfully')
            form.save()
        return render(request,'register.html',{'form':form}) 

def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')



def product(request,product_id):
    product_item= models.product.objects.filter(product_id=product_id)
    product_detail=product_item[0].product_details.split('_')
    if request.user.is_authenticated:
        cart_user= request.user
        cart_items= models.cart.objects.filter(user=cart_user)
        params={'product':product_item[0],'details':product_detail,'num_of_cart_items':len(cart_items)}
        params['nav_links']=True
        params['price_without_discount']=2000
        params['discount_percent']=(params['price_without_discount']-params['product'].product_price)/params['price_without_discount']*100
    return render(request,'product.html',params)


def cartView(request):
    params={'nav_links':True}
    if request.user.is_authenticated:
        cart_user= request.user
        cart_items= models.cart.objects.filter(user=cart_user)
        products=[]
        total_price=0
        for item in cart_items:
            product={
                'id':item.product_id.product_id,
                'name':item.product_id.product_title,
                'price':item.product_id.product_price*item.quantity,
                'quantity':item.quantity,
                'image':item.product_id.image,
                'category':item.product_id.product_category.name
            }
            total_price+=product['price']
            products.append(product)
        params['products']=products
        params['total_number_of_items']=len(products)
        params['total_price']=total_price
        params['shipping']=100
        params['total_amount']=total_price+100
        params['num_of_cart_items']=len(products)
        return render(request,'cart.html',params)
    else:
        return redirect('login')


@cache_control(no_cache=True, no_store=True)
def addtocart(request,product_id):
    cart_user= request.user
    cart_product= models.product.objects.filter(product_id=product_id)[0]
    if not models.cart.objects.filter(user=cart_user,product_id=cart_product).exists():            
        quantity=1
        #create new cart
        c=models.cart(user=cart_user,product_id=cart_product,quantity=quantity)
        c.save()
    else:
        #update cart
        cart_item= models.cart.objects.filter(user=cart_user,product_id=cart_product)[0]
        cart_item.quantity+=1
        cart_item.save()
    return redirect('cart')

def removefromcart(request,product_id):
    cart_user= request.user
    cart_product= models.product.objects.filter(product_id=product_id)[0]
    if models.cart.objects.filter(user=cart_user,product_id=cart_product)[0].quantity==1:          
        #delete cart
        cart_item= models.cart.objects.filter(user=cart_user,product_id=cart_product)[0]
        cart_item.delete()
    else:
        #update cart
        cart_item= models.cart.objects.filter(user=cart_user,product_id=cart_product)[0]
        cart_item.quantity-=1
        cart_item.save()
    return redirect('cart')



class addProfile(View):
    def get(self,request):
        form = detailsform()
        print(form)
        return render(request,'addprofile.html',{'form':form})
    def post(self,request):
        form = detailsform(request.POST)
        user= request.user
        form.instance.user_id=user
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,'addprofile.html',{'form':form})

class editProfile(View):
    def get(self,request):
        user= request.user
        details= models.billing_details.objects.filter(user_id=user)[0]
        form = detailsform(instance=details)
        return render(request,'addprofile.html',{'form':form})
    def post(self,request):
        user= request.user
        details= models.billing_details.objects.filter(user_id=user)[0]
        form = detailsform(request.POST,instance=details)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,'addprofile.html',{'form':form})

def profile(request):
    params={'nav_links':True}
    if request.user.is_authenticated:
        user= request.user
        params['user']=user
        cart_items= models.cart.objects.filter(user=user)
        params['num_of_cart_items']=len(cart_items)
        if models.billing_details.objects.filter(user_id=user).exists():
            details= models.billing_details.objects.filter(user_id=user)[0]
            details={

                'name':details.name,
                'phone':details.phone,
                'email':details.email,
                'address':details.address,
                'city':details.city,
                'state':details.state,
                'pin':details.pin
            }
            params['details']=details
        else:
            params['details']=None
        return render(request,'profile.html',params)
    else:
        return redirect('login')



def checkout(request):
    params={'nav_links':True}
    if request.user.is_authenticated:
        params['ifDetails']=False
        if models.billing_details.objects.filter(user_id=request.user).exists():
            params['ifDetails']=True
        else:
            messages.warning(request,'Please add your details to proceed')
        total_price=0
        for item in models.cart.objects.filter(user=request.user):
            total_price+=item.product_id.product_price*item.quantity
        shipping=100
        total_amount=total_price+shipping
        params['total_price']=total_price
        params['shipping']=shipping
        params['total_amount']=total_amount

        user= request.user
        params['user']=user
        if models.billing_details.objects.filter(user_id=user).exists():
            details= models.billing_details.objects.filter(user_id=user)[0]
            details={

                'name':details.name,
                'phone':details.phone,
                'email':details.email,
                'address':details.address,
                'city':details.city,
                'state':details.state,
                'pin':details.pin
            }
            params['details']=details
        else:
            params['details']=None
        return render(request,'checkout.html',params)
    else:
        return redirect('login')

