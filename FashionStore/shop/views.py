from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Product, Category
from django.db.models import Q
from cart.cart import Cart
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product




# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def producto(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'productdet.html',{'product':product})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user to DB automatically
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Go to login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            # After successful login → Home page
            return redirect("home")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

def wishlist(request):
    return render(request, 'wishlist.html')

def home_view(request):
    return render(request, 'home.html')

def category(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    return render(request, 'category.html', {'products': products})

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()


        if searched == "":
            messages.warning(request, "Please enter a product name.")
            return render(request, "search.html", {})


        products = Product.objects.filter(
    Q(name__icontains=searched) |
    Q(category__name__icontains=searched)
)


        if not products:
            messages.error(request, "No matching products found.")
            return render(request, "search.html", {})


        return render(request, "search.html", {'searched': products})


    return render(request, "search.html", {})



def cart(request):
    return render(request, 'cart.html')



class ProductAPI(APIView):
   
    def get(self, request, id=None):
        if id:
            product = product.objects.get(id=id)
            serializer = ProductSerializer(Product)
            return Response(serializer.data)
        product = Product.objects.all()
        serializer = ProductSerializer(Product, many=True)
        return Response(serializer.data)




    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student created successfully!"})
        return Response(serializer.errors)




    def put(self, request, id):
        student = Product.objects.get(id=id)
        serializer = ProductSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Product updated successfully!"})
        return Response(serializer.errors)




    def delete(self, request, id):
        student = Product.objects.get(id=id)
        student.delete()
        return Response({"msg": "Product deleted successfully!"})
    

    def patch(self, request, id):




        student = Product.objects.get(id=id)




        serializer = ProductSerializer(
            student,
            data=request.data,
            partial=True
        )




        if serializer.is_valid():
            serializer.save()
            return Response({
                "msg": "Student partially updated successfully!"
            })




        return Response(serializer.errors, status=400)














