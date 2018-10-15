from rest_framework import serializers
from shop.models import Currencies, Product, DeliveryType, Category, Contractor, Order, OrderPositions, WishList, \
    ProductPriceList, DeliveryPriceList

class CurrenciesSerializer(serializers.Serializer):

    id = serializers.IntegerField(label='ID', read_only=True)
    Name = serializers.CharField(required=False, allow_blank=False, allow_null=False, max_length=100)
    Mnemonic = serializers.CharField(required=False, allow_null=False, allow_blank=False, max_length=3)
    ExchangeRate = serializers.FloatField(required=True)
    LesserPlaces = serializers.IntegerField(required=True, allow_null=False)

    def create(self, validated_data):
        """
        Create and return a new Currency, given the validated data
        :param validated_data:
        :return:
        """
        return Currencies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Currency' instance, given the validated data.
        :param instance:
        :param validated_data:
        :return:
        """
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Mnemonic = validated_data('Mnemonic', instance.Mnemonic)
        instance.ExchangeRate = validated_data('ExchangeRate', instance.ExchangeRate)
        instance.LesserPlaces = validated_data('LesserPlaces', instance.LesserPlaces)
        instance.save()
        return instance
