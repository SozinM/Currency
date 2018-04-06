# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from quickstart.models import Currency
from quickstart.serializers import CurrencySerializer

from datetime import date,timedelta

class Currency_list(viewsets.ModelViewSet):
    """
    List today currency
    """
    '''
    try:
        queryset = Currency.objects.filter(timestamp = date.today())
    except:
        try:
            queryset = Currency.objects.filter(timestamp = date.today()-timedelta(days=1))
        except:
        #there is 503 error page
    '''
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer



