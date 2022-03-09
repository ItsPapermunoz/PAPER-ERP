# File Data

_author_ = "Rodrigo Muñoz"
_Version_ = "'Alpha'"

# Imports

from Essentials import *
from Accounts import *
from Products import *
from Sales import *
from Accounting import *

# Variable Definitions

clients = load_db("Clients.dat")
products = load_db("Products.dat")
contacts = load_db("Contacts.dat")
companies_list = load_db("Companies.dat")
active_company, active_user = login_company(companies_list)
sales = load_db("Sales.dat")
books = load_db("Books.dat")

# Function Definitions

def sales_menu():
    print("\n----- Menu Ventas -----\n")

def products_menu():
    print("\n----- Menu Productos -----\n")

def accounting_menu(books):
    while True:
        print("\n----- Menu Contabilidad -----\n")
        options = ["Nueva Cuenta Contable", "Nueva Transacción", "Borrar Cuenta", "Borrar Transacción", "Reportes", "Salir"]
        sel = display_menu(options)
        if sel == len(options):
            break
        if sel == 1:
            x = new_book(books)
        elif sel == 2:
            x = new_transaction(books)
        elif sel == 3:
            del_book(books)
        elif sel == 4:
            del_tran(books)
        elif sel == 5:
            reports_accounting(books)
        
def accounts_menu(clients_list):
    while True:
        options = ['Nueva Cuenta', 'Nuevo Contacto', 'Eliminar Cuenta', ]
        sel = display_menu(options, 'Menu Clientes y Proovedores')
        if sel == len(options):
            break
        if sel == 1:
            pass

def main_menu(clients, products, contacts, companies_list, active_company, active_user, sales, books):
    while True:
        options = ["Ventas", "Productos", "Contabilidad", "Clientes y Proovedores", "Salir"]
        sel = display_menu(options, "PAPER ERP")
        if sel == len(options):
            print("Gracias por haber utilizado PAPER ERP. Hasta pronto!")
            break
        if sel == 1:
            sales_menu()
        elif sel == 2:
            products_menu()
        elif sel == 3:
            accounting_menu(books)
        elif sel == 4:
            accounts_menu(clients)
        else:
            print("Opción no encontrada...")

        
# Main

main_menu(clients, products, contacts, companies_list, active_company, active_user, sales, books)
