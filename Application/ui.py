def make_product(self):
    print("\nSeleccione el tipo de producto:")
    print("1. Fertilizante")
    print("2. Antibiótico")

    product_type_selection = input("Opción: ")

    if product_type_selection == "1":
        colombian_agricultural_certificate = input("Registro ICA: ")
        product_name = input("Nombre del producto: ")
        application_frequency_description = input("Frecuencia de aplicación (Ej: Cada 15 días): ")
        try:
            frequency_in_days = int(''.join(filter(str.isdigit, application_frequency_description)) or 15)
        except:
            frequency_in_days = 15
            
        product_value = float(input("Valor del producto: "))
        last_application_date_string = input("Fecha de última aplicación (AAAA-MM-DD): ")
        
        from datetime import datetime
        try:
            last_application_date = datetime.strptime(last_application_date_string, "%Y-%m-%d").date()
        except:
            print("❌ Formato de fecha inválido, usando fecha actual.")
            from datetime import date
            last_application_date = date.today()

        from Model.fertilizer_control import Fertilizer
        product = Fertilizer(colombian_agricultural_certificate, product_name, frequency_in_days, product_value, last_application_date)
        print(f"✅ Producto '{product_name}' creado con éxito.")
        return product

    elif product_type_selection == "2":
        antibiotic_name = input("Nombre del antibiótico: ")
        dose_with_units = input("Dosis (Ej: 400Kg, 500Kg): ")
        animal_type = input("Tipo de animal (Bovino, Porcino, Caprino): ")
        product_price = float(input("Precio del producto: "))

        from Model.antibiotic import Antibiotic
        product = Antibiotic(antibiotic_name, dose_with_units, animal_type, product_price)
        print(f"✅ Antibiótico '{antibiotic_name}' creado con éxito.")
        return product

    else:
        print("❌ Opción inválida.")
        return None