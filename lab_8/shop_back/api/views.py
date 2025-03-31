from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .models import Product


# Create your views here.

class EasyBuyApi(APIView):
    def get(self,request):
        allProducts = Product.objects.all().values() 
        return Response({"Message": "List of products.", "Product list": allProducts })
    
    def get(self,request):
        Product.objects.create(
            id = request.id["id"],
            name = request.data["name"],
            price = request.data["price"],
            description = request.data["description"],
            count = request.data["count"],
            is_active = request.data["is_active"]
        )
        
        Product = Product.objects.all().filter(id = request.data["id"]).values()
        return Response({"Message": "New book added", "Product": Product})


