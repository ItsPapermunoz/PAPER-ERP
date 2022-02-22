# File Data

_author_ = "Rodrigo Muñoz"
_Version_ = "Alpha"

# Imports

from Essentials import *
from Accounts import *
from Products import *
from Sales import *

# Variable Definitions

clients = load_db("Clients.dat")
products = load_db("Products.dat")
contacts = load_db("Contacts.dat")
companies_list = load_db("Companies.dat")
active_company, active_user = login_company(companies_list)
sales = load_db("Sales.dat")
books = load_db("Books.dat")

# Function Definitions

def main_menu():
    print("\n----- PAPER ERP ---- Versión: {} Creado por: {}\nEmpresa: {} Usuario: {}".format(_Version_, _author_, active_company.rs, active_user.name))

# Main

main_menu()
