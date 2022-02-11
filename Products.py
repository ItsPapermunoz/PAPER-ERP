# File data

_author_ = "Rodrigo Muñoz"
_Version_ = "Alpha"

# imports

from Company_data import*
from Accounts import *

# Class

class Product():
    def __init__(self, clave, desc, price, tax, cost, inventory, supplier):
        self.clave = clave
        self.desc = desc
        self.price = price
        self.tax = tax
        self.cost = cost
        self.inventory = inventory
        self.supplier = supplier

def new_product(products_list, clients_list):
    while True:
        print("\n----- Nuevo Producto -----\n")
        x = len(products_list) + 1
        if x == 1:
            clave = "{}0001".format(company_prefix)
        elif x >= 2:
            clave = "{}000{}".format(company_prefix, x)
        elif x >= 10:
            clave = "{}00{}".format(company_prefix, x)
        elif x >= 100:
            clave = "{}0{}".format(company_prefix, x)
        else:
            clave = str(x)
        desc = input("Ingrese nombre del nuevo producto: ")
        price = input("Ingrese precio de lista del nuevo producto: ")
        tax = float(input("Ingrese la tasa de impuestos del nuevo producto (Debe ser un decimal): "))
        supplier = input("Ingrese Clave de proveedor, si la desconoce ingrese 'NO': ")
        if supplier == "NO":
            list_clients(clients_list, 2, "SUPP")
            supplier = input("Ingrese la clave del proveedor deseado: ")
            supplier = list_clients(clients_list, 1, supplier)
        else:
            supplier = list_clients(clients_list, 1, supplier)
        if supplier:
            print("\nVerifique la información de su nuevo producto: ")
            print("Clave: {}\nNombre: {}\nPrecio: {}\nTasa de impuesto: {}\nProveedor: {}".format(clave, desc, price, tax, supplier.rs))
            confirm = int(input("\n1. Confirmar alta de producto.\n2. Corregir información.\n3. Cancelar alta de producto.\n"))
            if confirm == 1:
                product = Product(clave, desc, price, tax, 0, 0, supplier)
                products_list.append(product)
                write_db(products_list, "Products.dat")
                break
            elif confirm == 2:
                continue
            else:
                print("Alta cancelada.")
                break
        else:
            pass


    

    
    
    

