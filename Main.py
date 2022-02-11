# File Data

_author_ = "Rodrigo Muñoz"
_Version_ = "Alpha"

# Imports

from Essentials import *
from Accounts import *
from Products import *

# Variable Definitions

clients = load_db("Clients.dat")
products = load_db("Products.dat")
contacts = load_db("Contacts.dat")

# Function Definitions

# Main

new_product(products, clients)

