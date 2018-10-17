from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """
        Product model

        Title, Image, Description, Category, Likes, Price is held in ProductPriceList model where is associated with
        currency

        Likes are stored in WishList model

        Image is held in S3 Storage / Google Cloud Storage (however, depending on configuration it is available
        to upload files to /media catalog.

    """
    Title = models.CharField(max_length=500)
    Image = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Price = models.FloatField()


class DeliveryType(models.Model):
    """
        Delivery Type

        Holds information about delivery and if delivery has a fixed price (IsPercent value informs controller if
        total sum shall be calculated on the basis of percent of total or if the fixed amount must be added to the
        total value of positions.

        IsPercent is type of models.NullBooleanField() temporarily. Not all database systems may support that value.
    """
    Title = models.CharField(max_length=500)
    IsPercent = models.NullBooleanField()
    PercentValue = models.FloatField()
    Price = models.FloatField()


class Category(models.Model):
    """
        Category model

        Nothing big to do a description here. :)
    """
    Title = models.CharField(max_length=100)


class Contractor(models.Model):
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    """
        Order model

        Method of delivery and contractor are associated to the order.
        The order has its positions stated in shop.models.OrderPositions model.


    """
    # Contractor
    Number = models.BigIntegerField()
    MethodOfDelivery = models.ForeignKey(DeliveryType, on_delete=models.PROTECT)
    Timestamp = models.DateTimeField(auto_created=True)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    Count = models.IntegerField(default=1)


class WishList(models.Model):
    Contractor = models.ForeignKey(Contractor, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.CASCADE)

    """
        Holds wishlist of the products.

        User clicks "like" on the product and it gets added to user's wish list.
    """
