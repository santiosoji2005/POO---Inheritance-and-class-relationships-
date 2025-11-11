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
from Model.invoice import Invoice
from Model.client import Client
from Model.line_item import LineItem


class TestDebugCompositionAndInheritance(unittest.TestCase):

    def test_discover_attributes(self):
        """DEBUG: Descubrir los atributos reales de las clases"""
        print("\n" + "="*60)
        print("🔍 DESCUBRIENDO ATRIBUTOS REALES")
        print("="*60)
        
        # Crear objetos de prueba
        client = Client("Test Client", "12345678")
        antibiotic = Antibiotic("Test Antibiotic", "500", "Bovino", 100.0)
        invoice = Invoice(client, date.today())
        
        print("📊 ATRIBUTOS DE CLIENT:")
        for attr in dir(client):
            if not attr.startswith('_'):
                try:
                    value = getattr(client, attr)
                    print(f"   {attr}: {value} (tipo: {type(value).__name__})")
                except:
                    print(f"   {attr}: [Error al acceder]")
        
        print("\n📊 ATRIBUTOS DE INVOICE:")
        for attr in dir(invoice):
            if not attr.startswith('_'):
                try:
                    value = getattr(invoice, attr)
                    if not callable(value):  # Excluir métodos
                        print(f"   {attr}: {value} (tipo: {type(value).__name__})")
                except:
                    print(f"   {attr}: [Error al acceder]")
        
        print("\n📊 ATRIBUTOS DE ANTIBIOTIC:")
        for attr in dir(antibiotic):
            if not attr.startswith('_'):
                try:
                    value = getattr(antibiotic, attr)
                    if not callable(value):
                        print(f"   {attr}: {value} (tipo: {type(value).__name__})")
                except:
                    print(f"   {attr}: [Error al acceder]")
        
        breakpoint()  # Pausa para ver los atributos descubiertos

    def test_debug_inheritance_hierarchy(self):
        """DEBUG: Mostrar herencia de objetos"""
        print("\n" + "="*60)
        print("🔍 DEBUG HERENCIA - JERARQUÍA DE CLASES")
        print("="*60)
        
        # Crear instancias para debug
        antibiotic = Antibiotic("Amoxi", "500", "Bovino", 100.0)
        fertilizer = Fertilizer("ICA123", "FertiGold", 15, 75.0, date.today())
        pest_control = PestControl("ICA456", "PestStop", 30, 7, 120.0)
        
        # Mostrar información de herencia
        print(f"\n📊 INFORMACIÓN DE HERENCIA:")
        print(f"Antibiotic: {type(antibiotic)}")
        print(f"   MRO: {Antibiotic.__mro__}")
        
        print(f"\nFertilizer: {type(fertilizer)}")
        print(f"   MRO: {Fertilizer.__mro__}")
        
        print(f"\nPestControl: {type(pest_control)}")
        print(f"   MRO: {PestControl.__mro__}")
        
        print("🔄 Pausa para inspeccionar HERENCIA - Presiona F10 para continuar")
        breakpoint()  # DEBUG BREAKPOINT 1 - Herencia

    def test_debug_object_composition(self):
        """DEBUG: Mostrar composición de objetos en Invoice"""
        print("\n" + "="*60)
        print("🔍 DEBUG COMPOSICIÓN - OBJETOS ANIDADOS")
        print("="*60)
        
        # Crear objetos para composición
        client = Client("Maria Garcia", "87654321")
        antibiotic = Antibiotic("Tetraciclina", "450", "Porcino", 85.0)
        fertilizer = Fertilizer("ICA789", "NutriPlant", 20, 60.0, date.today())
        
        # Crear LineItems (composición)
        line_item1 = LineItem(antibiotic, 2)
        line_item2 = LineItem(fertilizer, 3)
        
        # Crear Invoice (composición múltiple)
        invoice = Invoice(client, date.today())
        invoice.add_item(line_item1)
        invoice.add_item(line_item2)
        
        # Mostrar estructura usando atributos genéricos
        print(f"\n📊 ESTRUCTURA DE COMPOSICIÓN:")
        print(f"Invoice: {invoice}")
        print(f"   Client object: {invoice.client}")
        print(f"   Total Items: {len(invoice.items)}")
        print(f"   Total: ${invoice.total}")
        
        print(f"\n📦 DETALLE DE ITEMS (Composición):")
        for i, item in enumerate(invoice.items, 1):
            print(f"   Item {i}: {type(item).__name__}")
            print(f"      Product: {type(item.product).__name__}")
            print(f"      Quantity: {item.quantity}")
            print(f"      Line Total: ${item.line_total}")
            
            # Mostrar todos los atributos del producto
            product = item.product
            print(f"      Product Attributes:")
            for attr in dir(product):
                if not attr.startswith('_') and not callable(getattr(product, attr)):
                    try:
                        value = getattr(product, attr)
                        print(f"        {attr}: {value}")
                    except:
                        pass
        
        print("🔄 Pausa para inspeccionar COMPOSICIÓN - Presiona F10 para continuar")
        breakpoint()  # DEBUG BREAKPOINT 2 - Composición

    def test_debug_complex_composition(self):
        """DEBUG: Composición compleja con múltiples niveles"""
        print("\n" + "="*60)
        print("🔍 DEBUG COMPOSICIÓN COMPLEJA - MÚLTIPLES NIVELES")
        print("="*60)
        
        # Crear múltiples productos
        products = [
            Antibiotic("Penicilina", "500", "Bovino", 95.0),
            Fertilizer("ICA111", "GrowFast", 10, 45.0, date.today()),
            PestControl("ICA222", "BugTerminator", 25, 5, 110.0),
            Antibiotic("Oxitetraciclina", "480", "Caprino", 88.0)
        ]
        
        # Crear cliente y factura
        client = Client("Carlos Rodriguez", "11223344")
        invoice = Invoice(client, date.today())
        
        # Agregar productos a la factura
        for i, product in enumerate(products, 1):
            line_item = LineItem(product, i)
            invoice.add_item(line_item)
        
        # Mostrar resumen de composición sin usar atributos específicos
        print(f"\n🎯 RESUMEN DE COMPOSICIÓN:")
        print(f"Client object: {client}")
        print(f"Factura con {len(invoice.items)} items compuestos")
        print(f"Valor Total: ${invoice.total}")
        
        print(f"\n🔗 CADENA DE COMPOSICIÓN:")
        print(f"Invoice → {len(invoice.items)} LineItems → {len(products)} Products")
        
        # Contar tipos de productos
        product_types = {}
        for item in invoice.items:
            product_type = type(item.product).__name__
            product_types[product_type] = product_types.get(product_type, 0) + 1
        
        print(f"\n📊 DISTRIBUCIÓN DE PRODUCTOS:")
        for p_type, count in product_types.items():
            print(f"   {p_type}: {count} instancias")
        
        print("🔄 Pausa para inspeccionar COMPOSICIÓN COMPLEJA - Presiona F10")
        breakpoint()  # DEBUG BREAKPOINT 3 - Composición Compleja


if __name__ == "__main__":
    unittest.main()