from ast import Num
from django.contrib import admin
from psycopg2 import Date
from .models import Item, NumericItem, TextItem
# Register your models here.
admin.site.register(Item)
admin.site.register(NumericItem)
admin.site.register(TextItem)