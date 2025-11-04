import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

from products import Product
from product_features import ControlProduct

class PestControl(ControlProduct):
    def __init__(self, colombian_agricultural_certificate, product_name, frequency_in_days, withdrawal_period_in_days, product_price):
        super().__init__(colombian_agricultural_certificate, product_name, frequency_in_days, product_price)
        if withdrawal_period_in_days < 0:
            raise ValueError("El período de retiro no puede ser negativo.")
        self.withdrawal_period_in_days = withdrawal_period_in_days
