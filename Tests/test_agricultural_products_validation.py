import sys
import os
import unittest
from datetime import date

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from Model.products import Product
from Model.antibiotic import Antibiotic
from Model.fertilizer_control import Fertilizer
from Model.pest_control import PestControl
from Model.product_features import ControlProduct


class TestAgriculturalProductsValidation(unittest.TestCase):

    def test_create_basic_product(self):
        product = Product("Test del Producto", 50.0)
        self.assertEqual(product.name, "Test del Producto")
        self.assertEqual(product.price, 50.0)

    def test_product_invalid_price(self):
        with self.assertRaises(ValueError):
            Product("Test del Producto", -10.0)

    def test_product_empty_name(self):
        with self.assertRaises(ValueError):
            Product("", 50.0)

    def test_create_valid_antibiotic(self):
        antibiotic = Antibiotic("Amoxi", "500", "Porcino", 100.0)
        self.assertEqual(antibiotic.name, "Amoxi")
        self.assertEqual(antibiotic.dose_kg, 500)
        self.assertEqual(antibiotic.animal_type, "Porcino")
        self.assertEqual(antibiotic.price, 100.0)

    def test_antibiotic_invalid_dose(self):
        with self.assertRaises(ValueError):
            Antibiotic("Amoxi", "300", "Porcino", 100.0)
        
        with self.assertRaises(ValueError):
            Antibiotic("Amoxi", "700", "Porcino", 100.0)

    def test_antibiotic_invalid_animal_type(self):
        with self.assertRaises(ValueError):
            Antibiotic("Amoxi", "500", "Ave", 100.0)

    def test_create_valid_fertilizer(self):
        application_date = date(2024, 1, 1)
        fertilizer = Fertilizer("ICA123", "Fertilizante A", 15, 75.0, application_date)
        
        self.assertEqual(fertilizer.name, "Fertilizante A")
        self.assertEqual(fertilizer.colombian_agricultural_certificate, "ICA123")
        self.assertEqual(fertilizer.frequency_in_days, 15)
        self.assertEqual(fertilizer.price, 75.0)
        self.assertEqual(fertilizer.last_application_date, application_date)

    def test_create_valid_pest_control(self):
        pest_control = PestControl("ICA456", "Control Plagas A", 30, 7, 120.0)
        
        self.assertEqual(pest_control.name, "Control Plagas A")
        self.assertEqual(pest_control.colombian_agricultural_certificate, "ICA456")
        self.assertEqual(pest_control.frequency_in_days, 30)
        self.assertEqual(pest_control.withdrawal_period_in_days, 7)
        self.assertEqual(pest_control.price, 120.0)

    def test_pest_control_invalid_withdrawal_period(self):
        with self.assertRaises(ValueError):
            PestControl("ICA456", "Control Plagas A", 30, -5, 120.0)

    def test_control_product_invalid_frequency(self):
        with self.assertRaises(ValueError):
            PestControl("ICA456", "Control Plagas A", 0, 7, 120.0)

    def test_control_product_empty_colombian_agricultural_certificate(self):
        with self.assertRaises(ValueError):
            PestControl("", "Control Plagas A", 30, 7, 120.0)

    def test_product_inheritance(self):
        antibiotic = Antibiotic("Test", "500", "Bovino", 100.0)
        self.assertIsInstance(antibiotic, object)
        
        fertilizer = Fertilizer("ICA123", "Test", 15, 50.0, date.today())
        self.assertIsInstance(fertilizer, object)
        
        pest_control = PestControl("ICA456", "Test", 30, 7, 80.0)
        self.assertIsInstance(pest_control, object)


if __name__ == "__main__":
    unittest.main()