"""
    Module:
        simple_shop.simple_shop.populate

    Purpose:
        Populating database with example data.
        This package contains example data for sample_shop application.
"""

from simple_shop.shop.models import Category, Client, Currency, DeliveryAddress, DeliveryPrice, \
    DeliveryType, Order, OrderPositions, Product, PriceList

from random import randint, randrange


def populate_Currency(currencies):
    """

    :param currencies: list of dictionaries
    :return: None

    This function is not data-safe, it may overwrite data if used many times or on existing data
    """
    for element in currencies:
        currency = Currency()
        currency.Name = element['Name']
        currency.Mnemonic = element['Mnemonic']
        currency.ExchangeRate = float(element['ExchangeRate'])
        currency.save()


def populate_Categories(categories):
    """

    :param categories: list of dictionaries
    :return: None

    This function is not data-safe, it may overwrite data if used many times or on existing data
    """
    for element in categories:
        category = Category()
        category.Name = element['Name']
        category.save()


def populate_Products(products):
    """

    :param products: list of dictionaries
    :return: None

    This function applies all elements found in given dictionary and populates database with random prices depending on
    currencies currently available in system.
    Remember, that this function is for testing purposes only and it does not imply any exchange rates. So, i.e.
    you may experience Bike at 100 PLN but 5000 EUR. This is not an error, this is because of usage of randint function
    to randomly assign price.

    This function is not data-safe, it may overwrite data if used many times or on existing data
    """
    for element in products:
        product = Product()
        product.Title = element['Title']
        product.Description = element['Description']
        product.Image = element['Image']
        product.save()
        currencies = Currency.objects.all()
        for currency in currencies:
            price = PriceList()
            price.relatedCurrency = currency
            price.relatedProduct = product
            price.value = randint(100, 10000)
            price.save()


def populate_Delivery(deliveryTypes):
    """
    :parameter deliveryTypes : list of dictionaries
    :return: None

    This function is not data-safe, it may overwrite data if used many times or on existing data
    """
    for element in deliveryTypes:
        deliveryType = DeliveryType()
        deliveryType.Name = element['Name']
        deliveryType.save()


def populate_data():
    '''
    This function populates database with example data
    :return: None
    '''
    try:
        Currencies = [
            {
                'Name': "Polski zloty",
                'Mnemonic': 'PLN',
                'ExchangeRate': 1
            },
            {
                'Name': "EURO",
                'Mnemonic': 'EUR',
                'ExchangeRate': 0.25
            },
            {
                'Name': "Pound sterling",
                'Mnemonic': 'GBP',
                'ExchangeRate': 0.20
            },
        ]
        populate_Currency(Currencies)
        Categories = [
            {
                'Title': 'Bikes'
            },
            {
                'Title': 'Hi-Fi'
            },
            {
                'Title': 'Computers'
            },
            {
                'Title': 'Notebooks'
            },
            {
                'Title': 'Clothing'
            },
            {
                'Title': 'Networking'
            }
        ]
        populate_Categories(Categories)
        Deliveries = [
            {
                'Name': 'FedEx International',
                'Price' : [{'Value' : '100', 'Currency' : 'PLN'}]
            },
            {
                'Name': 'DHL',
                'Price' : [{'Value' : '20', 'Currency' : 'PLN'}]
            },
            {
                'Name': 'International Postal Service (FREE)',
                'Price' : [{'Value' : '0', 'Currency' : 'PLN'}],
            },
            {
                'Name': 'Own Transport',
                'Price' : [{'Value' : 0, 'Currency' : 'PLN'}, {'Value' : 100, 'Currency' : 'EUR'}]
            }
        ]
        populate_Delivery(Deliveries)
        Products = [
            {
                'Title': 'Acer Predator Helios 300',
                'Categories': ['Computers', 'Notebooks'],
                'Price': [{'Value': '5699', 'Currency': 'PLN'}, {'Value': '1500', 'Currency': 'EUR'},
                          {'Value': '900', 'Currency': 'GBP'}]
            },
            {
                'Title': 'Generic Bluetooth Adaptor',
                'Categories': ['Computers', 'Networking'],
                'Price': [{'Value': '100', 'Currency': 'PLN'}]
            },
            {
                'Title': 'Generic Bicycle',
                'Categories': ['Bikes'],
                'Price' : [{'Value':'500', 'Currency': 'GBP'}]
            },
            {
                'Title': 'Superlux HD 669',
                'Categories': ['Computers', 'Hi-Fi'],
                'Price' : [{'Value' : '100', 'Currency' : 'PLN'}]
            }
        ]
        populate_Products(Products)
        print('Data populated properly.')
    except:
        print('Data populated improperly.')


populate_data()
