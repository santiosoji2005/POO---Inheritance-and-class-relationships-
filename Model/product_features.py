import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

from products import Product

class ControlProduct(Product):
    def __init__(self, colombian_agricultural_certificate, product_name, frequency_in_days, product_price):
        super().__init__(product_name, product_price)
        if not colombian_agricultural_certificate:
            raise ValueError("Registro ICA no puede estar vacío.")
        if frequency_in_days <= 0:
            raise ValueError("La frecuencia debe ser mayor que cero.")
        self.colombian_agricultural_certificate = colombian_agricultural_certificate
        self.frequency_in_days = frequency_in_days