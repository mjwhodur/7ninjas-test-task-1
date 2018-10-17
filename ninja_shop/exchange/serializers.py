from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, DeliveryType, Category, Order, WishList


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """

    """
    #orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # This relation is not needed because we don't want to show
    # all orders to everyone - shopping shall be private

    class Meta:
        model = Product
        fields = ('id', 'Title', 'Image', 'Description', 'Price',)


class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ('Title', 'IsPercent', 'PercentValue', 'Price')


class OrderSerializer(serializers.ModelSerializer):
    """
        We don't provide serialization of User field, because it will be handled automatically in the view: the view
        automatically assigns proper user prohibiting to create order for someone else.
    """
    class Meta:
        model = Order
        fields = ('ReferenceNumber', 'MethodOfDelivery', 'Product', 'Count')


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('Contractor', 'Product')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class UserSerializer(serializers.ModelSerializer):
    ###
    ### Because is a reverse relationship on the User model, it will not be included by default, when using ModelSerializer Class
    ### so we need to add an explicit field for it.
    ###

    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username')
