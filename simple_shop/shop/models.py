from django.db import models

# Create your models here.

class Client(models.Model):
    UserName = models.CharField(max_length=500)


class DeliveryAddress(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    Name = models.CharField(max_length=500)
    Street = models.CharField(max_length=200, null=True)
    StreetNumber = models.CharField(max_length=100)
    AptSuiteNumber = models.CharField(max_length=20, null=True)
    PostalCode = models.CharField(max_length=10)
    Country = models.CharField(max_length=100)


class Product(models.Model):
    Title = models.CharField(max_length=200, null=False)
    Image = models.CharField(max_length=500, null=True)
    Description = models.CharField(max_length=500)

class Currency(models.Model):
    Name = models.CharField(max_length=500)
    Mnemonic = models.CharField(max_length=3)
    ExchangeRate = models.FloatField(default=1)

class PriceList(models.Model):
    relatedProduct = models.ForeignKey(Product, on_delete=models.deletion.PROTECT)
    relatedCurrency = models.ForeignKey(Currency, on_delete=models.deletion.PROTECT)

class DeliveryType(models.Model):
    Name = models.CharField(max_length=500)

class DeliveryPrice(models.Model):
    Name = models.CharField(max_length=500)
    Currency = models.ForeignKey(Currency, on_delete=models.deletion.CASCADE)
    Price = models.FloatField(default=0)

class Category(models.Model):
    Name = models.CharField(max_length=50, null=False)

class Order(models.Model):
    Number = models.CharField(max_length=50, null=False)
    DeliveryAddress = models.ForeignKey(DeliveryAddress, on_delete=models.deletion.PROTECT)
    DeliveryType = models.ForeignKey(DeliveryType, on_delete=models.deletion.PROTECT)
    Currency = models.ForeignKey(Currency, on_delete=models.deletion.PROTECT)

class OrderPositions(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.PROTECT)
    DeliveryType = models.ForeignKey(DeliveryType, on_delete=models.deletion.PROTECT)

class WishList(models.Model):
    User = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.deletion.CASCADE)

