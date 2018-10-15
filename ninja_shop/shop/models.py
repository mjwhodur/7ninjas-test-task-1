from django.db import models


class Currencies(models.Model):
    """
        Currency model

        Model for holding information about currency and their exchange rates

        Thanks to Exchange rate application will automatically convert prices to their values i.e.:

            def SetPrice(Product, Currency, value, [list of prices set on form]):
                Get Currency Exchange rate
                basePrice = value / Currency.ExchangeRate
                for currency in Currency.objects.all()
                    #   ... some important stuff here
                    #   For each currency the price is set automatically
                    #   except for prices implicitly set.
                    #
                    #

        If user has a shop in Poland, but does not sell in Poland, and sets the price in EURO, not in PLN and sets
        its exchange rate, the price will be calculated to PLN (base currency with exchange rate == 1) and then
        converted into each currency supported by the shop, if not set implicitly.

        LesserPlaces : models.IntegerField contains information about how many
        digits are after dot in the currency. I.e. in PLN or EURO 2, in HUF 2, CHK 1, SEK 0
    """
    Name = models.CharField(max_length=500)
    Mnemonic = models.CharField(max_length=3)
    ExchangeRate = models.FloatField()
    LesserPlaces = models.IntegerField()


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


class Category(models.Model):
    """
        Category model

        Nothing big to do a description here. :)
    """
    Title = models.CharField(max_length=100)


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
    Timestamp = models.DateTimeField(auto_created=True)


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

        SetImplicitly field states if price was set directly by the user, so the shop won't affect changes.
        However, if the user deletes the value, the SetImplicitly flag would be set to False, stating
        the shop has to automatically handle the conversion process.
    """
    Product = models.ForeignKey(Product)
    Currency = models.ForeignKey(Currencies)
    Price = models.FloatField()
    SetImplicitly = models.BooleanField()


class DeliveryPriceList(models.Model):
    """
        Delivery price list

        Holds prices regarding delivery methods and currencies.
        These values may be automatically calculated

        SetImplicitly field states if price was set directly by the user, so the shop won't affect changes.
        However, if the user deletes the value, the SetImplicitly flag would be set to False, stating
        the shop has to automatically handle the conversion process.

    """
    DeliveryMethod = models.ForeignKey(DeliveryType)
    Currency = models.ForeignKey(Currencies)
    Price = models.FloatField()

