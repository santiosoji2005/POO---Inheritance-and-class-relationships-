from Application.ui import Agro_Shop_ui

def main():
    app = Agro_Shop_ui()

    while True:
        app.show_menu()
        option = input("Seleccione una opción: ")

        if option == "1":
            app.registrar_cliente()
        elif option == "2":
            app.crear_producto()
        elif option == "3":
            app.generar_factura()
        elif option == "4":
            app.ver_facturas()
        elif option == "5":
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
