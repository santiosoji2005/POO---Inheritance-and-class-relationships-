import sys
import os
import unittest
from datetime import date

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from Model.antibiotic import Antibiotic
from Model.fertilizer_control import Fertilizer
from Model.client import Client
from Model.invoice import Invoice
from Model.line_item import LineItem


class TestAgriculturalSalesProcess(unittest.TestCase):

    def setUp(self):
        self.client = Client("Juan Perez", "12345678")
        self.date = date(2024, 1, 15)

    def test_create_invoice(self):
        invoice = Invoice(self.client, self.date)
        self.assertEqual(invoice.client, self.client)
        self.assertEqual(invoice.date, self.date)
        self.assertEqual(len(invoice.items), 0)
        self.assertEqual(invoice.total, 0)

    def test_add_antibiotic_product(self):
        antibiotic = Antibiotic("Amoxi", "500", "Porcino", 100.0)
        invoice = Invoice(self.client, self.date)
        invoice.add_product(antibiotic)
        
        self.assertEqual(len(invoice.items), 1)
        self.assertEqual(invoice.total, 100.0)

    def test_add_fertilizer_product(self):
        from datetime import date as date_class
        fertilizer = Fertilizer("ICA123", "Fertilizante A", 15, 75.0, date_class(2024, 1, 1))
        invoice = Invoice(self.client, self.date)
        invoice.add_product(fertilizer)
        
        self.assertEqual(len(invoice.items), 1)
        self.assertEqual(invoice.total, 75.0)

    def test_calculate_total_multiple_products(self):
        antibiotic = Antibiotic("Amoxi", "500", "Porcino", 100.0)
        fertilizer = Fertilizer("ICA123", "Fertilizante A", 15, 75.0, date(2024, 1, 1))
        
        invoice = Invoice(self.client, self.date)
        invoice.add_product(antibiotic)
        invoice.add_product(fertilizer)
        invoice.calculate_total()
        
        self.assertEqual(len(invoice.items), 2)
        self.assertEqual(invoice.total, 175.0)
        self.assertEqual(invoice.total_value, 175.0)

    def test_line_item_quantity(self):
        antibiotic = Antibiotic("Amoxi", "500", "Porcino", 100.0)
        item = LineItem(antibiotic, 3)
        
        self.assertEqual(item.quantity, 3)
        self.assertEqual(item.line_total, 300.0)

    def test_invoice_with_line_items(self):
        antibiotic = Antibiotic("Amoxi", "500", "Porcino", 100.0)
        fertilizer = Fertilizer("ICA123", "Fertilizante A", 15, 75.0, date(2024, 1, 1))
        
        item1 = LineItem(antibiotic, 2)
        item2 = LineItem(fertilizer, 1)
        
        invoice = Invoice(self.client, self.date)
        invoice.add_item(item1)
        invoice.add_item(item2)
        
        self.assertEqual(invoice.total, 275.0)


if __name__ == "__main__":
    unittest.main()