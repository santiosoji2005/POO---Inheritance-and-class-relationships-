import sys
import os


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from typing import List
from Model.products import Product
from Model.antibiotic import Antibiotic
from Model.fertilizer_control import Fertilizer
from Model.pest_control import PestControl
from .db import products_db

def add_product(product):
    products_db.append(product)
    return product

def list_products() -> List[Product]:
    return list(products_db)

def find_products_by_name(name: str):
    return [p for p in products_db if p.name.lower() == name.lower()]

def remove_product(product):
    if product in products_db:
        products_db.remove(product)
        return True
    return False
