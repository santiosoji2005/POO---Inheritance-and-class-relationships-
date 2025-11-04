import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

from datetime import date
from line_item import LineItem

class Invoice:
    def __init__(self, client, invoice_date):
        self.client = client
        self.date = invoice_date
        self.items = []
        self.total_value = 0

    def add_item(self, item):
        self.items.append(item)

    def add_product(self, product):
        item = LineItem(product, 1)
        self.items.append(item)

    def calculate_total(self):
        self.total_value = self.total

    @property
    def total(self):
        return sum(item.line_total for item in self.items)
    
    @property
    def products(self):
        return [item.product for item in self.items]