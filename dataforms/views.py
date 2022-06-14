from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from items.models import Item, NumericItem, TextItem
from .models import DataForm
from itertools import chain



