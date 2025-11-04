import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

from datetime import date
from product_features import ControlProduct

class Fertilizer(ControlProduct):
    def __init__(self, colombian_agricultural_certificate, product_name, frequency_in_days, product_price, last_application_date):
        super().__init__(colombian_agricultural_certificate, product_name, frequency_in_days, product_price)
        if not isinstance(last_application_date, date):
            raise ValueError("La última aplicación debe ser una fecha.")
        self.last_application_date = last_application_date