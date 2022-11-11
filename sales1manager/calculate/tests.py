from django.test import TestCase, Client


from django.shortcuts import render, redirect
from django.http import HttpResponse
import openpyxl 
from openpyxl.utils.dataframe import dataframe_to_rows
from pandas import DataFrame
from uploadtodb.models import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def somethingTest(self):

        contents = tbl_invoice_daily.objects.all().count()
        print(contents)