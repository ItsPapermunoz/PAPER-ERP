""" Sales Module """

# Imports

from asyncore import write
from itertools import product
from Essentials import *
from Products import *
from Accounts import *


# Variable Definitions

kind_of_sales = {1: "Cotización", 2: "Pedido", 3: "Factura", 4: "Nota de Crédito"}

kind_of_status = {1: "En Proceso", 2: "Terminado", 3: "Cancelado"}

# Class Definitions

def sum_lines(attribute, item_list):
    i = 0 
    if attribute == 0:
        for item in item_list:
            i += item.subtotal
    elif attribute == 1:
        for item in item_list:
            i += item.disc
    elif attribute == 2:
        for item in item_list:
            i += item.tax
    return i

def sel_client(clients_list):
    while True:
            client = int(input("\n1. Ingrese Clave de cliente\n2. Lista de clientes.\n3. Cancelar\nSeleccione una opción: "))
            if client == 2:
                lookup_client(clients_list)
                continue
            elif client == 3:
                return None
            else:
                client = input("Ingrese Clave: ")
                client = lookup_client(clients_list, 1, client)
                if client:
                    return client
                else:
                    continue
class Line_item():
    def __init__(self, qty, sku, price, disc_1, disc_2, tax_rate):
        self.qty = qty
        self.sku = sku
        self.price = price
        self.subtotal = qty * price
        self.disc_1 = disc_1
        self.disc_2 = disc_2
        self.disc = self.price * self.disc_1 * self.disc_2
        self.tax_rate = tax_rate
        self.tax = (self.subtotal - self.disc) * self.tax_rate
        self.total = (self.subtotal - self.disc) * (self.tax_rate + 1)
    def report(self, line_number):
        print("{}. Cantidad: {} SKU: {} Precio: {} Total: {}".format(line_number, self.qty, self.sku.desc, self.price, self.total))

class Sale:
    def __init__(self, sales_list, active_company, clients_list, products_list):
        print("\n----- Nueva Venta -----\n")
        self.kind = int(input("1. {}\n2. {}\n3. {}\n4. {}\nSeleccione una opción: ".format(kind_of_sales[1], kind_of_sales[2], kind_of_sales[3], kind_of_sales[4])))
        self.ref = "{}-000{}".format(active_company.company_prefix, len(sales_list) + 1)
        self.lines = []
        self.status = kind_of_status[1]
        self.subtotal = sum_lines(0, self.lines)
        self.disc = sum_lines(1, self.lines)
        self.tax = sum_lines(2, self.lines)
        self.total = self.subtotal - self.disc + self.tax
        self.trans = []
        self.client = sel_client(clients_list)
        self.add_line(products_list)
        sales_list.append(self)
        write_db(sales_list, "Sales.dat")
        print("Venta: {} registrada exitosamente!".format(self.ref))
            
    def upgrade(self):
        if self.kind != 3 or 4:
            self.kind += 1
            print('Tipo de venta actualizado a {}'.format(self.kind))
        else:
            print("No es posible cambiar tipo de venta a facturas o notas de crédito.")
    
    def add_line(self, products_list):
        while True:
            qty = int(input("Cantidad: "))
            while True:
                product = input("1. Ingrese SKU\n2. Ingrese LISTA para ver lista de productos\nProducto: ")
                if product == "LISTA":
                    lookup_products(products_list)
                else:
                    sku = lookup_products(products_list, product)
                    break
            price = float(input("Precio de lista: {}\nPrecio: ".format(sku.price)))
            disc_1 = float((int(input("Descuento 1: "))) / 100)
            disc_2 = float((int(input("Descuento 2: "))) / 100)
            if disc_1 == 0:
                disc_1 = 1
            if disc_2 == 0:
                disc_2 = 1
            tax_rate = sku.tax
            line = Line_item(qty, sku, price, disc_1, disc_2, tax_rate)
            self.lines.append(line)
            self.subtotal += line.subtotal
            self.disc += line.disc
            self.tax += line.tax
            self.total += line.total
            confirm = int(input("1. Ingresar otro producto o servicio\n2. Terminar Lineas."))
            if confirm == 1:
                continue
            else:
                break

    def report(self):
        print("\n ----- {}: {} -----\n".format(self.kind, self.ref))
        print("Cliente: {}\nStatus: {}\n".format(self.client.name, self.status))
        print("Lineas:")
        i = 1
        for line in self.lines:
            line.report(i)
            i += 1
        print('Subtotal: {}\nDescuento: {}\nImpuestos: {}\nTotal: {}'.format(self.subtotal, self.disc, self.tax, self.total))


# Function definitions

