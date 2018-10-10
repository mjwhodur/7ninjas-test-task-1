from django.db import models


class Currencies(models.Model):
    """
        Currency model

        Model for holding information about currency and their exchange rates
    """
    Name = models.CharField()
    Mnemonic = models.CharField()
    ExchangeRate = models.FloatField()


class Product(models.Model):
    """
        Product model

        Title, Image, Description, Category, Likes, Price is held in ProductPriceList model where is associated with
        currency

        Likes are stored in WishList model

        Image is held in S3 Storage / Google Cloud Storage (however, depending on configuration it is available
        to upload files to /media catalog.

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
    # Contractor
    Number = models.BigIntegerField()
    MethodOfDelivery = models.ForeignKey(DeliveryType)
    Currency = models.ForeignKey(Currencies)
    Timestamp = models.DateTimeField()


class OrderPositions(models.Model):
    """
        Positions of the order model

        Method of delivery does not count on its positions. Total is calculated after summing positions and chosen
        delivery method.

        The following list consists of positions with selected options and retains the price if the sales assistant
        changes the price after placing order
    """
    Order = models.ForeignKey(Order)
    Product = models.ForeignKey(Product)
    Quantity = models.IntegerField()
    Price = models.FloatField()


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
    Product = models.ForeignKey(Product)
    Currency = models.ForeignKey(Currencies)
    Price = models.FloatField()


class DeliveryPriceList(models.Model):
    """
        Delivery price list

        Holds prices regarding delivery methods and currencies.
        These values may be automatically calculated
    """
    DeliveryMethod = models.ForeignKey(DeliveryType)
    Currency = models.ForeignKey(Currencies)
    Price = models.FloatField()
