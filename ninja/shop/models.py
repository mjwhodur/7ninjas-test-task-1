from django.db import models

# Create your models here.

class Currencies(models.Model):
    """
        Model for holding information about currency and their exchange rates
    """
    pass

class Product(models.Model):
    """
        Product model

        Title, Image, Description, Category, Likes, Price is held in ProductPriceList model where is associated with
        currency

        Likes are stored in WishList model
    """
    Title = models.CharField()
    Image = models.CharField()
    Description = models.CharField()


class DeliveryType(models.Model):
    """
        Delivery Type

        Holds information about delivery and if delivery has a fixed price (IsPercent value informs controller if
        total sum shall be calculated on the basis of percent of total or if the fixed amount must be added to the
        total value of positions.

        IsPercent is type of models.NullBooleanField() temporarily. Not all database systems may support that value.
    """
    Title = models.CharField()
    IsPercent = models.NullBooleanField()
    PercentValue = models.FloatField()

class Category(models.Model):
    """
        Category model

        Nothing big to do a description here. :)
    """
    Title = models.CharField()

class Order(models.Model):
    """
        Order model

        Method of delivery and contractor are associated to the order.
        The order has its positions stated in shop.models.OrderPositions model.


    """
    #Contractor
    Number = models.BigIntegerField()
    MethodOfDelivery = models.ForeignKey(DeliveryType)
    Currency = models.ForeignKey(Currencies)

class OrderPositions(models.Model):
    """
        Positions of the order model

        Method of delivery does not count on its positions. Total is calculated after summing positions and chosen
        delivery method.

        The following list consists of positions with selec
    """
    pass

class WishList(models.Model):
    """
        Holds wishlist of the products.

        User clicks "like" on the product and it gets added to user's wish list.
    """
    pass


class ProductPriceList(models.Model):
    """
        Product price list

        Holds prices regarding different currencies.
        These values may be automatically calculated
    """
    pass

class DeliveryPriceList(models.Model):
    pass

