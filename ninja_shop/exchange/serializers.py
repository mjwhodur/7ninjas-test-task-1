from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, DeliveryType, Category, Order, WishList


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'Title', 'Image', 'Description', 'Price')


class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ('Title', 'IsPercent', 'PercentValue', 'Price')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('Number', 'MethodOfDelivery', 'Timestamp', 'Product', 'Count', 'User')


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('Contractor', 'Product')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ###
    ### Because is a reverse relationship on the User model, it will not be included by default, when using ModelSerializer Class
    ### so we need to add an explicit field for it.
    ###

    #snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username')
