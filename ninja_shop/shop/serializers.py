from rest_framework import serializers
from ninja_shop.shop.models import Product, DeliveryType, Category, Contractor, Order, WishList


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'Title', 'Image', 'Description', 'Price')


class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ('Title', 'IsPercent', 'PercentValue', 'Price')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('Number', 'MethodOfDelivery', 'Timestamp', 'Product', 'Count')


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('Contractor', 'Product')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
