from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from shop.models import Product
# from shop.serializers import ProductSerializer


# class PlaceOrder(generics.CreateAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer

#    def perform_create(self, serializer):
#        serializer.save()
from exchange.serializers import ProductSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'products': reverse('api-product-list', request=request, format=format)
    })


@api_view(['POST'])
def PlaceOrder():
    return None


@api_view(['GET'])
def user_list(request, format=None):
    pass


@api_view(['GET'])
def UserList():
    return None
from exchange.models import Product


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
