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
        UserName: type of django.db.models.CharField with max length of 500 having enough
    """
    UserName = models.CharField(max_length=500)


class DeliveryAddress(models.Model):
    """
    Model: DeliveryAddress

    Description:
        Model holding data of delivery addresses. One client may have many delivery addressess (i.e. home, company, va-
        cation address).

    Columns:
        Client
        Name
        Street
        StreetNumber
        AptSuiteNumber
        PostalCode
        Country
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

    Columns:
        Title
        Image
        Description
    """
    Title = models.CharField(max_length=200, null=False)
    Image = models.CharField(max_length=500, null=True)
    Description = models.CharField(max_length=500)

class Currency(models.Model):
    """
    Model: Currency

    Description:

    Columns:
        Name
        Mnemonic
        Exchange
    """
    Name = models.CharField(max_length=500)
    Mnemonic = models.CharField(max_length=3)
    ExchangeRate = models.FloatField(default=1)

class PriceList(models.Model):
    """
    Models: PriceList

    Description:

    Columns:
        relatedProduct
        relatedCurrency
    """
    relatedProduct = models.ForeignKey(Product, on_delete=models.deletion.PROTECT)
    relatedCurrency = models.ForeignKey(Currency, on_delete=models.deletion.PROTECT)

class DeliveryType(models.Model):
    """
    Model: DeliveryType

    Description:

    Columns:
        Name
    """
    Name = models.CharField(max_length=500)

class DeliveryPrice(models.Model):
    """
    Model: DeliveryPrice

    Description:

    Columns:
        Name
        Currency
        Price
    """
    Name = models.CharField(max_length=500)
    Currency = models.ForeignKey(Currency, on_delete=models.deletion.CASCADE)
    Price = models.FloatField(default=0)

class Category(models.Model):
    """
    Model: Category

    Description:

    Columns:
        Name
    """
    Name = models.CharField(max_length=50, null=False)

class Order(models.Model):
    """
    Model: Order

    Description:

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

    Columns:
        Order
        Product
        DeliveryType
    """
    Order = models.ForeignKey(Order, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.PROTECT)
    DeliveryType = models.ForeignKey(DeliveryType, on_delete=models.deletion.PROTECT)

class WishList(models.Model):
    """
    Model WishList

    Description:

    Columns:
        User
        Product
    """
    User = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.CASCADE)