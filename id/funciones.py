# Sistema Integral de Gestión de Inventario y Ventas para Tienda de Electrónica
# Este programa permite gestionar productos, registrar ventas y generar reportes dinámicos

import json
import csv
from datetime import datetime

# ============================================================================
# ESTRUCTURA DE DATOS GLOBAL
# ============================================================================
# Diccionario principal que almacena todos los productos del inventario
# Estructura: {id_producto: {nombre, marca, categoria, precio, stock, garantia}}
inventory = {}

# Lista que almacena todas las ventas realizadas
# Cada venta es un diccionario con: cliente, tipo_cliente, producto_id, cantidad, fecha, descuento, total
sales = []

# Contador global para asignar IDs unicos a cada producto
product_id_counter = 1

# ============================================================================
# FUNCIONES DE INICIALIZACION
# ============================================================================

def load_initial_products():
    """
    Carga 5 productos iniciales en el inventario al iniciar el sistema.
    Esta funcion se ejecuta una sola vez al comenzar el programa.
    """
    global product_id_counter
    
    # Lista de productos precargados con toda su informacion
    initial_products = [
        {"name": "Samsung Galaxy S23", "brand": "Samsung", "category": "Smartphones", "price": 899.99, "stock": 50, "warranty": 24},
        {"name": "iPhone 15 Pro", "brand": "Apple", "category": "Smartphones", "price": 1199.99, "stock": 30, "warranty": 12},
        {"name": "Sony WH-1000XM5", "brand": "Sony", "category": "Headphones", "price": 399.99, "stock": 75, "warranty": 12},
        {"name": "MacBook Pro 14", "brand": "Apple", "category": "Laptops", "price": 1999.99, "stock": 20, "warranty": 12},
        {"name": "LG OLED C3 55", "brand": "LG", "category": "TVs", "price": 1499.99, "stock": 15, "warranty": 24}
    ]
    
    # Insertar cada producto en el inventario con su ID correspondiente
    for product in initial_products:
        inventory[product_id_counter] = product
        product_id_counter += 1
    
    print("System initialized with 5 products.")

# ============================================================================
# FUNCIONES DE GESTION DE INVENTARIO
# ============================================================================

def add_product():
    """
    Registra un nuevo producto en el inventario.
    Solicita todos los datos necesarios al usuario y valida las entradas.
    """
    global product_id_counter
    
    print("\n--- ADD NEW PRODUCT ---")
    
    try:
        # Solicitar y validar cada campo del producto
        name = input("Product name: ").strip()
        if not name:
            print("Error: Product name cannot be empty.")
            return
        
        brand = input("Brand: ").strip()
        if not brand:
            print("Error: Brand cannot be empty.")
            return
        
        category = input("Category: ").strip()
        if not category:
            print("Error: Category cannot be empty.")
            return
        
        # Validar que el precio sea un numero positivo
        price = float(input("Unit price: "))
        if price <= 0:
            print("Error: Price must be greater than zero.")
            return
        
        # Validar que el stock sea un numero entero no negativo
        stock = int(input("Stock quantity: "))
        if stock < 0:
            print("Error: Stock cannot be negative.")
            return
        
        # Validar que la garantia sea un numero entero positivo
        warranty = int(input("Warranty (months): "))
        if warranty <= 0:
            print("Error: Warranty must be greater than zero.")
            return
        
        # Crear el diccionario del producto y agregarlo al inventario
        inventory[product_id_counter] = {
            "name": name,
            "brand": brand,
            "category": category,
            "price": price,
            "stock": stock,
            "warranty": warranty
        }
        
        print(f"Product added successfully with ID: {product_id_counter}")
        product_id_counter += 1
        
    except ValueError:
        print("Error: Invalid input. Please enter correct data types.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_products():
    """
    Muestra todos los productos registrados en el inventario.
    Presenta la informacion en formato tabular para facil lectura.
    """
    print("\n--- INVENTORY LIST ---")
    
    if not inventory:
        print("No products in inventory.")
        return
    
    # Recorrer el diccionario de inventario y mostrar cada producto
    print(f"{'ID':<5} {'Name':<25} {'Brand':<15} {'Category':<15} {'Price':<10} {'Stock':<8} {'Warranty':<10}")
    print("-" * 100)
    
    for product_id, product in inventory.items():
        print(f"{product_id:<5} {product['name']:<25} {product['brand']:<15} {product['category']:<15} "
              f"${product['price']:<9.2f} {product['stock']:<8} {product['warranty']} months")

def update_product():
    """
    Actualiza la informacion de un producto existente.
    Permite modificar cualquier campo excepto el ID.
    """
    print("\n--- UPDATE PRODUCT ---")
    
    try:
        # Solicitar el ID del producto a actualizar
        product_id = int(input("Enter product ID to update: "))
        
        # Verificar que el producto exista en el inventario
        if product_id not in inventory:
            print("Error: Product not found.")
            return
        
        # Mostrar informacion actual del producto
        print(f"Current product: {inventory[product_id]['name']}")
        
        # Solicitar nuevos valores (permitir dejar en blanco para mantener el valor actual)
        name = input(f"New name (current: {inventory[product_id]['name']}): ").strip()
        brand = input(f"New brand (current: {inventory[product_id]['brand']}): ").strip()
        category = input(f"New category (current: {inventory[product_id]['category']}): ").strip()
        price_input = input(f"New price (current: {inventory[product_id]['price']}): ").strip()
        stock_input = input(f"New stock (current: {inventory[product_id]['stock']}): ").strip()
        warranty_input = input(f"New warranty (current: {inventory[product_id]['warranty']}): ").strip()
        
        # Actualizar solo los campos que no esten vacios
        if name:
            inventory[product_id]['name'] = name
        if brand:
            inventory[product_id]['brand'] = brand
        if category:
            inventory[product_id]['category'] = category
        if price_input:
            price = float(price_input)
            if price > 0:
                inventory[product_id]['price'] = price
        if stock_input:
            stock = int(stock_input)
            if stock >= 0:
                inventory[product_id]['stock'] = stock
        if warranty_input:
            warranty = int(warranty_input)
            if warranty > 0:
                inventory[product_id]['warranty'] = warranty
        
        print("Product updated successfully.")
        
    except ValueError:
        print("Error: Invalid input.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def delete_product():
    """
    Elimina un producto del inventario.
    Solicita confirmacion antes de proceder con la eliminacion.
    """
    print("\n--- DELETE PRODUCT ---")
    
    try:
        # Solicitar el ID del producto a eliminar
        product_id = int(input("Enter product ID to delete: "))
        
        # Verificar que el producto exista
        if product_id not in inventory:
            print("Error: Product not found.")
            return
        
        # Mostrar producto y solicitar confirmacion
        print(f"Product to delete: {inventory[product_id]['name']}")
        confirm = input("Are you sure you want to delete this product? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            del inventory[product_id]
            print("Product deleted successfully.")
        else:
            print("Deletion cancelled.")
    
    except ValueError:
        print("Error: Invalid product ID.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# ============================================================================
# FUNCIONES DE GESTION DE VENTAS
# ============================================================================

def calculate_discount(customer_type):
    """
    Calcula el porcentaje de descuento segun el tipo de cliente.
    
    Parametros:
        customer_type (str): Tipo de cliente (regular, vip, employee)
    
    Retorna:
        float: Porcentaje de descuento (0.0 a 1.0)
    """
    # Diccionario que mapea tipos de cliente a sus descuentos correspondientes
    discounts = {
        "regular": 0.0,    # Sin descuento
        "vip": 0.15,       # 15% de descuento
        "employee": 0.25   # 25% de descuento
    }
    
    # Retornar el descuento correspondiente o 0 si el tipo no existe
    return discounts.get(customer_type.lower(), 0.0)

def register_sale():
    """
    Registra una nueva venta en el sistema.
    Valida stock disponible, aplica descuentos y actualiza el inventario automaticamente.
    """
    print("\n--- REGISTER SALE ---")
    
    try:
        # Solicitar informacion del cliente
        customer = input("Customer name: ").strip()
        if not customer:
            print("Error: Customer name cannot be empty.")
            return
        
        # Solicitar y validar tipo de cliente
        print("Customer types: regular, vip, employee")
        customer_type = input("Customer type: ").strip().lower()
        if customer_type not in ["regular", "vip", "employee"]:
            print("Error: Invalid customer type.")
            return
        
        # Mostrar productos disponibles para facilitar la seleccion
        view_products()
        
        # Solicitar ID del producto a vender
        product_id = int(input("\nEnter product ID to sell: "))
        
        # Verificar que el producto exista
        if product_id not in inventory:
            print("Error: Product not found.")
            return
        
        # Solicitar cantidad a vender
        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            return
        
        # Verificar stock disponible
        if inventory[product_id]['stock'] < quantity:
            print(f"Error: Insufficient stock. Available: {inventory[product_id]['stock']}")
            return
        
        # Calcular valores de la venta
        unit_price = inventory[product_id]['price']
        discount_rate = calculate_discount(customer_type)
        subtotal = unit_price * quantity
        discount_amount = subtotal * discount_rate
        total = subtotal - discount_amount
        
        # Obtener fecha actual
        sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Crear registro de venta
        sale = {
            "customer": customer,
            "customer_type": customer_type,
            "product_id": product_id,
            "product_name": inventory[product_id]['name'],
            "brand": inventory[product_id]['brand'],
            "quantity": quantity,
            "unit_price": unit_price,
            "subtotal": subtotal,
            "discount_rate": discount_rate,
            "discount_amount": discount_amount,
            "total": total,
            "date": sale_date
        }
        
        # Agregar venta a la lista y actualizar inventario
        sales.append(sale)
        inventory[product_id]['stock'] -= quantity
        
        # Mostrar resumen de la venta
        print("\n--- SALE SUMMARY ---")
        print(f"Customer: {customer} ({customer_type})")
        print(f"Product: {inventory[product_id]['name']}")
        print(f"Quantity: {quantity}")
        print(f"Unit price: ${unit_price:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount ({discount_rate*100:.0f}%): -${discount_amount:.2f}")
        print(f"Total: ${total:.2f}")
        print("Sale registered successfully.")
        
    except ValueError:
        print("Error: Invalid input.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_sales():
    """
    Muestra el historial completo de todas las ventas realizadas.
    Presenta la informacion ordenada cronologicamente.
    """
    print("\n--- SALES HISTORY ---")
    
    if not sales:
        print("No sales registered.")
        return
    
    # Recorrer lista de ventas y mostrar cada una
    for index, sale in enumerate(sales, 1):
        print(f"\nSale #{index}")
        print(f"Date: {sale['date']}")
        print(f"Customer: {sale['customer']} ({sale['customer_type']})")
        print(f"Product: {sale['product_name']} (ID: {sale['product_id']})")
        print(f"Brand: {sale['brand']}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Unit price: ${sale['unit_price']:.2f}")
        print(f"Subtotal: ${sale['subtotal']:.2f}")
        print(f"Discount: -${sale['discount_amount']:.2f}")
        print(f"Total: ${sale['total']:.2f}")
        print("-" * 50)

# ============================================================================
# FUNCIONES DE REPORTES
# ============================================================================

def top_selling_products():
    """
    Genera reporte de los 3 productos mas vendidos.
    Agrupa las ventas por producto y las ordena por cantidad vendida.
    """
    print("\n--- TOP 3 BEST-SELLING PRODUCTS ---")
    
    if not sales:
        print("No sales data available.")
        return
    
    # Diccionario para acumular cantidades vendidas por producto
    product_sales = {}
    
    # Recorrer todas las ventas y sumar cantidades por producto
    for sale in sales:
        product_id = sale['product_id']
        if product_id in product_sales:
            product_sales[product_id]['quantity'] += sale['quantity']
            product_sales[product_id]['revenue'] += sale['total']
        else:
            product_sales[product_id] = {
                'name': sale['product_name'],
                'quantity': sale['quantity'],
                'revenue': sale['total']
            }
    
    # Ordenar productos por cantidad vendida (descendente) y tomar los 3 primeros
    # Lambda function para extraer la cantidad como criterio de ordenamiento
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1]['quantity'], reverse=True)[:3]
    
    # Mostrar los top 3 productos
    if sorted_products:
        for rank, (product_id, data) in enumerate(sorted_products, 1):
            print(f"{rank}. {data['name']} (ID: {product_id})")
            print(f"   Units sold: {data['quantity']}")
            print(f"   Revenue: ${data['revenue']:.2f}\n")
    else:
        print("No sales data available.")

def sales_by_brand():
    """
    Genera reporte de ventas agrupadas por marca.
    Muestra unidades vendidas e ingresos totales por cada marca.
    """
    print("\n--- SALES BY BRAND ---")
    
    if not sales:
        print("No sales data available.")
        return
    
    # Diccionario para acumular ventas por marca
    brand_sales = {}
    
    # Agrupar ventas por marca
    for sale in sales:
        brand = sale['brand']
        if brand in brand_sales:
            brand_sales[brand]['units'] += sale['quantity']
            brand_sales[brand]['revenue'] += sale['total']
        else:
            brand_sales[brand] = {
                'units': sale['quantity'],
                'revenue': sale['total']
            }
    
    # Mostrar resultados ordenados alfabeticamente por marca
    for brand in sorted(brand_sales.keys()):
        data = brand_sales[brand]
        print(f"\nBrand: {brand}")
        print(f"Total units sold: {data['units']}")
        print(f"Total revenue: ${data['revenue']:.2f}")

def calculate_revenue():
    """
    Calcula y muestra los ingresos brutos y netos del negocio.
    Ingreso bruto: suma de subtotales antes de descuentos
    Ingreso neto: suma de totales despues de descuentos
    """
    print("\n--- REVENUE REPORT ---")
    
    if not sales:
        print("No sales data available.")
        return
    
    # Lambda functions para calcular sumas de subtotales y totales
    # Estas funciones permiten operaciones agregadas de forma concisa
    gross_revenue = sum(map(lambda sale: sale['subtotal'], sales))
    net_revenue = sum(map(lambda sale: sale['total'], sales))
    total_discounts = gross_revenue - net_revenue
    
    print(f"Gross revenue (before discounts): ${gross_revenue:.2f}")
    print(f"Total discounts applied: ${total_discounts:.2f}")
    print(f"Net revenue (after discounts): ${net_revenue:.2f}")

def inventory_performance():
    """
    Evalua el rendimiento del inventario comparando stock actual con ventas.
    Calcula el porcentaje de inventario vendido por producto.
    """
    print("\n--- INVENTORY PERFORMANCE ---")
    
    if not sales:
        print("No sales data available.")
        return
    
    # Diccionario para acumular unidades vendidas por producto
    units_sold = {}
    
    for sale in sales:
        product_id = sale['product_id']
        if product_id in units_sold:
            units_sold[product_id] += sale['quantity']
        else:
            units_sold[product_id] = sale['quantity']
    
    # Mostrar rendimiento de cada producto vendido
    print(f"{'Product':<30} {'Sold':<10} {'Current Stock':<15} {'Performance':<15}")
    print("-" * 70)
    
    for product_id, sold in units_sold.items():
        if product_id in inventory:
            product = inventory[product_id]
            current_stock = product['stock']
            total_stock = sold + current_stock
            
            # Calcular porcentaje de inventario vendido
            if total_stock > 0:
                performance = (sold / total_stock) * 100
            else:
                performance = 0
            
            print(f"{product['name']:<30} {sold:<10} {current_stock:<15} {performance:.2f}%")

# ============================================================================
# FUNCIONES DE PERSISTENCIA DE DATOS (CSV, JSON, TXT)
# ============================================================================

def save_to_csv():
    """
    Guarda el inventario y las ventas en archivos CSV.
    CSV es un formato tabular facil de abrir en Excel y otras hojas de calculo.
    """
    try:
        # Guardar inventario en inventory.csv
        with open('inventory.csv', 'w', newline='', encoding='utf-8') as file:
            # Definir las columnas del archivo CSV
            fieldnames = ['id', 'name', 'brand', 'category', 'price', 'stock', 'warranty']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Escribir encabezados
            writer.writeheader()
            
            # Escribir cada producto como una fila
            for product_id, product in inventory.items():
                row = {'id': product_id}
                row.update(product)
                writer.writerow(row)
        
        # Guardar ventas en sales.csv
        if sales:
            with open('sales.csv', 'w', newline='', encoding='utf-8') as file:
                # Usar las claves del primer elemento de ventas como columnas
                fieldnames = sales[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(sales)
        
        print("Data saved to CSV files successfully.")
        
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def load_from_csv():
    """
    Carga el inventario y las ventas desde archivos CSV.
    Restaura el estado completo del sistema desde archivos guardados previamente.
    """
    global product_id_counter
    
    try:
        # Cargar inventario desde inventory.csv
        with open('inventory.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            inventory.clear()  # Limpiar inventario actual
            
            for row in reader:
                # Convertir tipos de datos apropiadamente
                product_id = int(row['id'])
                inventory[product_id] = {
                    'name': row['name'],
                    'brand': row['brand'],
                    'category': row['category'],
                    'price': float(row['price']),
                    'stock': int(row['stock']),
                    'warranty': int(row['warranty'])
                }
                # Actualizar contador para mantener IDs unicos
                if product_id >= product_id_counter:
                    product_id_counter = product_id + 1
        
        # Cargar ventas desde sales.csv
        try:
            with open('sales.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                sales.clear()  # Limpiar ventas actuales
                
                for row in reader:
                    # Convertir tipos de datos apropiadamente
                    sale = {
                        'customer': row['customer'],
                        'customer_type': row['customer_type'],
                        'product_id': int(row['product_id']),
                        'product_name': row['product_name'],
                        'brand': row['brand'],
                        'quantity': int(row['quantity']),
                        'unit_price': float(row['unit_price']),
                        'subtotal': float(row['subtotal']),
                        'discount_rate': float(row['discount_rate']),
                        'discount_amount': float(row['discount_amount']),
                        'total': float(row['total']),
                        'date': row['date']
                    }
                    sales.append(sale)
        except FileNotFoundError:
            print("Sales file not found. Starting with empty sales history.")
        
        print("Data loaded from CSV files successfully.")
        
    except FileNotFoundError:
        print("CSV files not found. Starting with empty database.")
    except Exception as e:
        print(f"Error loading from CSV: {e}")

def save_to_json():
    """
    Guarda el inventario y las ventas en archivos JSON.
    JSON mantiene la estructura de datos completa y es facil de leer.
    """
    try:
        # Preparar datos para guardar
        data = {
            'inventory': inventory,
            'sales': sales,
            'product_id_counter': product_id_counter
        }
        
        # Guardar en archivo JSON con formato legible (indent=4)
        with open('electronics_store.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
        print("Data saved to JSON file successfully.")
        
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def load_from_json():
    """
    Carga el inventario y las ventas desde un archivo JSON.
    Restaura el estado completo incluyendo el contador de IDs.
    """
    global product_id_counter
    
    try:
        with open('electronics_store.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Restaurar todas las estructuras de datos
        # Convertir claves de inventario a enteros (JSON guarda todo como strings)
        inventory.clear()
        for key, value in data['inventory'].items():
            inventory[int(key)] = value
        
        sales.clear()
        sales.extend(data['sales'])
        
        product_id_counter = data['product_id_counter']
        
        print("Data loaded from JSON file successfully.")
        
    except FileNotFoundError:
        print("JSON file not found. Starting with empty database.")
    except Exception as e:
        print(f"Error loading from JSON: {e}")

def save_to_txt():
    """
    Guarda el inventario y las ventas en archivos de texto plano.
    TXT es el formato mas simple y universal para lectura humana.
    """
    try:
        # Guardar inventario en inventory.txt
        with open('inventory.txt', 'w', encoding='utf-8') as file:
            file.write("=" * 80 + "\n")
            file.write("ELECTRONICS STORE - INVENTORY REPORT\n")
            file.write("=" * 80 + "\n\n")
            
            # Escribir encabezados
            file.write(f"{'ID':<5} {'Name':<25} {'Brand':<15} {'Category':<15} {'Price':<10} {'Stock':<8} {'Warranty':<10}\n")
            file.write("-" * 100 + "\n")
            
            # Escribir cada producto
            for product_id, product in inventory.items():
                file.write(f"{product_id:<5} {product['name']:<25} {product['brand']:<15} "
                          f"{product['category']:<15} ${product['price']:<9.2f} "
                          f"{product['stock']:<8} {product['warranty']} months\n")
        
        # Guardar ventas en sales.txt
        with open('sales.txt', 'w', encoding='utf-8') as file:
            file.write("=" * 80 + "\n")
            file.write("ELECTRONICS STORE - SALES REPORT\n")
            file.write("=" * 80 + "\n\n")
            
            if not sales:
                file.write("No sales registered.\n")
            else:
                # Escribir cada venta con formato detallado
                for index, sale in enumerate(sales, 1):
                    file.write(f"Sale #{index}\n")
                    file.write(f"Date: {sale['date']}\n")
                    file.write(f"Customer: {sale['customer']} ({sale['customer_type']})\n")
                    file.write(f"Product: {sale['product_name']} (ID: {sale['product_id']})\n")
                    file.write(f"Brand: {sale['brand']}\n")
                    file.write(f"Quantity: {sale['quantity']}\n")
                    file.write(f"Unit price: ${sale['unit_price']:.2f}\n")
                    file.write(f"Subtotal: ${sale['subtotal']:.2f}\n")
                    file.write(f"Discount: -${sale['discount_amount']:.2f}\n")
                    file.write(f"Total: ${sale['total']:.2f}\n")
                    file.write("-" * 80 + "\n\n")
        
        print("Data saved to TXT files successfully.")
        
    except Exception as e:
        print(f"Error saving to TXT: {e}")

def load_from_txt():
    """
    Nota: Cargar desde TXT es complejo debido a su formato libre.
    Se recomienda usar CSV o JSON para cargar datos.
    Esta funcion muestra un mensaje informativo.
    """
    print("Loading from TXT files is not implemented.")
    print("TXT format is designed for human reading, not data loading.")
    print("Please use JSON or CSV formats to load data.")

# ============================================================================
# MENU PRINCIPAL
# ============================================================================

def display_menu():
    """
    Muestra el menu principal del sistema con todas las opciones disponibles.
    """
    print("\n" + "=" * 60)
    print("ELECTRONICS STORE - INVENTORY AND SALES MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1.  Add product")
    print("2.  View products")
    print("3.  Update product")
    print("4.  Delete product")
    print("5.  Register sale")
    print("6.  View sales history")
    print("7.  Top 3 best-selling products")
    print("8.  Sales by brand")
    print("9.  Revenue report")
    print("10. Inventory performance")
    print("11. Save data to CSV")
    print("12. Load data from CSV")
    print("13. Save data to JSON")
    print("14. Load data from JSON")
    print("15. Save data to TXT")
    print("16. Exit")
    print("=" * 60)

def main():
    """
    Funcion principal que controla el flujo del programa.
    Muestra el menu y ejecuta las opciones seleccionadas por el usuario.
    """
    # Cargar productos iniciales al iniciar el sistema
    load_initial_products()
    
    # Bucle principal del programa
    while True:
        display_menu()
        
        try:
            # Solicitar opcion al usuario
            option = input("\nSelect an option: ").strip()
            
            # Ejecutar la funcion correspondiente a la opcion seleccionada
            if option == "1":
                add_product()
            elif option == "2":
                view_products()
            elif option == "3":
                update_product()
            elif option == "4":
                delete_product()
            elif option == "5":
                register_sale()
            elif option == "6":
                view_sales()
            elif option == "7":
                top_selling_products()
            elif option == "8":
                sales_by_brand()
            elif option == "9":
                calculate_revenue()
            elif option == "10":
                inventory_performance()
            elif option == "11":
                save_to_csv()
            elif option == "12":
                load_from_csv()
            elif option == "13":
                save_to_json()
            elif option == "14":
                load_from_json()
            elif option == "15":
                save_to_txt()
            elif option == "16":
                # Confirmar salida del programa
                confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("Thank you for using the system. Goodbye.")
                    break
            else:
                print("Invalid option. Please select a number from 1 to 16.")
        
        except KeyboardInterrupt:
            # Manejar interrupcion por teclado (Ctrl+C)
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            # Capturar cualquier error inesperado sin detener el programa
            print(f"Unexpected error: {e}")
            print("The program will continue running.")

# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================a