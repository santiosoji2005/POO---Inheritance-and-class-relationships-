import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from products import Product

class Antibiotic(Product):
    def __init__(self, name, dose_kg, animal_type, price):
        super().__init__(name, price)
        try:
            dose_value = int(dose_kg.replace('Kg', '').replace('kg', '').strip())
        except ValueError:
            raise ValueError("Dose must be a number.")
            
        if dose_value < 400 or dose_value > 600:
            raise ValueError("Dose must be between 400 and 600 Kg.")
        if animal_type not in ("Bovino", "Caprino", "Porcino"):
            raise ValueError("Invalid animal type.")
        self.dose_kg = dose_value
        self.animal_type = animal_type