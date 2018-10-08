from django.db import models


# Create your models here.

class Client(models.Model):
    """
    Model:
        Client

    Description:
        Model holding information about users, despite having the same data in django.contrib.auth.models.User

        This is because we don't want to alter the database if the django.contrib.auth.models will change if the
        library would be updated.

    Columns:
        UserName: type of django.db.models.CharField with max length of 500 having enough space to hold user's username
                  or i.e. key
    """
    UserName = models.CharField(max_length=500)


class DeliveryAddress(models.Model):
    """
    Model: DeliveryAddress

    Description:
        Model holding data of delivery addresses. One client may have many delivery addressess (i.e. home, company, va-
        cation address).

    Columns:
        Client: typeof django.db.models.ForeignKey
        Name: typeof django.db.models.CharField
        Street: typeof django.db.models.CharField
        StreetNumber: typeof django.db.models.CharField
        AptSuiteNumber: typeof django.db.models.CharField
        PostalCode: typeof django.db.models.CharField
        Country: typeof django.db.models.CharField
    """
    Client = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    Name = models.CharField(max_length=500)
    Street = models.CharField(max_length=200, null=True)
    StreetNumber = models.CharField(max_length=100)
    AptSuiteNumber = models.CharField(max_length=20, null=True)
    PostalCode = models.CharField(max_length=10)
    Country = models.CharField(max_length=100)


class Product(models.Model):
    """
    Model: Product

    Description:
        Model holding data of products. This model does not contain information about product's prices.
        This is because the seller may want to set different prices for different currencies.
        However, system enables to automatically convert between currencies if price in current currency is not set


    Columns:
        Title: typeof django.db.models.CharField
        Image: typeof django.db.models.CharField
        Description: typeof django.db.models.CharField
    """
    Title = models.CharField(max_length=200, null=False)
    Image = models.CharField(max_length=500, null=True)
    Description = models.CharField(max_length=500)


class Currency(models.Model):
    """
    Model: Currency

    Description:
        Model holding data of currencies. Allows automatic conversion between currencies, if needed. If not, user has to
        just set currency rate to 1 and it will be treated like base currency.

    Columns:
        Name: typeof django.db.models.CharField
        Mnemonic: typeof django.db.models.CharField
        Exchange: typeof django.db.models.CharField
    """
    Name = models.CharField(max_length=500)
    Mnemonic = models.CharField(max_length=3)
    ExchangeRate = models.FloatField(default=1)


class PriceList(models.Model):
    """
    Models: PriceList

    Description:

    Columns:
        relatedProduct: typeof django.db.models.ForeignKey in relation to shop.models.Product
        relatedCurrency typeof django.db.models.ForeignKey in relation to shop.models.Currency
    """
    relatedProduct = models.ForeignKey(Product, on_delete=models.deletion.PROTECT)
    relatedCurrency = models.ForeignKey(Currency, on_delete=models.deletion.PROTECT)
    value = models.FloatField(default=1)


class DeliveryType(models.Model):
    """
    Model: DeliveryType

    Description:
        Holds names of delivery types.
        NOTE: The Price is preserved in DeliveryPrice model depending on Currency.

    Columns:
        Name: typeof django.db.models.CharField
    """
    Name = models.CharField(max_length=500)


class DeliveryPrice(models.Model):
    """
    Model: DeliveryPrice

    Description:
        Holds delivery prices in different currencies.

    Columns:
        DeliveryType: typeof django.db.models.ForeignKey in relation to shop.models.DeliveryType
        Currency: typeof django.db.models.ForeignKey in relation to shop.models.Currency
        Price: typeof django.db.models.FloatField holding price data
    """
    DeliveryType = models.ForeignKey(DeliveryType, on_delete=models.deletion.CASCADE)
    Currency = models.ForeignKey(Currency, on_delete=models.deletion.CASCADE)
    Price = models.FloatField(default=0)


class Category(models.Model):
    """
    Model: Category

    Description:
        Holds information about categories available in system.

    Columns:
        Name: typeof django.db.models.CharField, holding data of Category name
    """
    Name = models.CharField(max_length=50, null=False)

class CategoriesList(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.CASCADE)

class Order(models.Model):
    """
    Model: Order

    Description:
        Holds basic data about placed orders.

    Columns:
        Number
        DeliveryAddress
        DeliveryType
        Currency
    """
    Number = models.CharField(max_length=50, null=False)
    DeliveryAddress = models.ForeignKey(DeliveryAddress, on_delete=models.deletion.PROTECT)
    DeliveryType = models.ForeignKey(DeliveryType, on_delete=models.deletion.PROTECT)
    Currency = models.ForeignKey(Currency, on_delete=models.deletion.PROTECT)


class OrderPositions(models.Model):
    """
    Model OrderPositions

    Description:
        Holds detailed information about positions of the order
        NOTE: The price may change if the staff change so we preserve the price and currency ordered
              Deletion of product does not remove the order's positions. Orders placed before deletion
              will be processed normally.

    Columns:
        Order
        Product
        Quantity
        Price
    """
    Order = models.ForeignKey(Order, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.PROTECT)
    Quantity = models.IntegerField(default=0)
    Price = models.FloatField(default=0)
    Currency = models.ForeignKey(Currency, on_delete=models.deletion.CASCADE)


class WishList(models.Model):
    """
    Model WishList

    Description:
        Holds wishlist.

    Columns:
        User: typeof django.db.models.ForeignKey with relation to shop.models.Client
        Product: typeof django.db.models.ForeignKey with relation to shop.models.Product
    """
    User = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.CASCADE)
