from rest_framework import serializers
from quickstart.models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    USD = serializers.FloatField(min_value=0)
    CZK = serializers.FloatField(min_value=0)
    PLN = serializers.FloatField(min_value=0)
    EUR = serializers.FloatField(min_value=0)
    
    class Meta:
        model = Currency
        fields = ('USD','PLN','EUR','CZK')



