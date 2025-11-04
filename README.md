Agro Shop - Sistema de Gestión para Farmacia Agrícola
🏢 Descripción General
Sistema de software para gestión de ventas e inventario de productos agropecuarios, específicamente diseñado para farmacias o distribuidoras agrícolas en Colombia.

🎯 Objetivo Principal
Gestionar el proceso completo de venta de productos agrícolas y pecuarios, cumpliendo con las regulaciones colombianas del ICA.

📦 Módulos Principales
1. Gestión de Productos
Productos Básicos (Product): Base común para todos los productos

Antibióticos (Antibiotic): Específicos para animales con control de dosis y tipo de animal

Fertilizantes (Fertilizer): Con registro ICA y control de fechas de aplicación

Control de Plagas (PestControl): Con períodos de retiro y frecuencia de aplicación

2. Proceso de Ventas
Facturación (Invoice): Sistema completo de facturas con múltiples productos

Clientes (Client): Gestión de información de clientes

Ítems de Línea (LineItem): Detalle de productos con cantidades en facturas

3. Características Técnicas
Validaciones de Negocio: Control de dosis, registros ICA, fechas de aplicación

Sistema de Precios: Cálculo automático de totales con múltiples productos

Herencia y Polimorfismo: Arquitectura extensible para nuevos tipos de productos

📋 Reglas de Negocio Implementadas
Validaciones Específicas:
Antibióticos: Dosis entre 400-600kg, tipos de animal válidos (Bovino, Porcino, Caprino)

Productos Controlados: Registro ICA obligatorio, frecuencia > 0 días

Fertilizantes: Control de fecha de última aplicación

Control de Plagas: Período de retiro no negativo

🔧 Tecnología
Lenguaje: Python

Testing: Framework unittest

Estructura: Arquitectura MVC (Modelo-Vista-Controlador)

Manejo de Fechas: Módulo datetime

🌍 Contexto Colombiano
El sistema está adaptado específicamente para el mercado colombiano con:

Cumplimiento de regulaciones ICA

Manejo de certificaciones agrícolas colombianas

Validaciones según normativas locales

✅ Estado Actual
Sistema funcional con:

Modelos de datos completos

Sistema de facturación operativo

Suite de tests automatizados

Validaciones de negocio implementadas

Este proyecto representa una solución completa para la gestión de farmacias veterinarias y distribuidoras de insumos agrícolas en Colombia.
