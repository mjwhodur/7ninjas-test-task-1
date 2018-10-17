from django.shortcuts import render

# Create your views here.
from rest_framework import generics


class ProductList(generics.ListAPIView):
    pass

class ProductDetail(object):
    pass


class ProductLike(object):
    pass


class Likes(object):
    pass


class PlaceOrder(object):
    pass