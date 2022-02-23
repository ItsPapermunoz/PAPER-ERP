# Accounting Module

# Imports

from Essentials import *

# Variables

kinds_tran = [ "INGRESO", "PAGO", "GASTO", "TRANSFERENCIA"]
kinds_book = ["EFECTIVO", "CUENTA BANCARIA", "CRÉDITO"]
# Classes

class Book:
    def __init__(self, clave,  name, kind):
        self.clave = clave
        self.name = name
        self.tran = []
        self.balance = 0
        self.kind = kind

    def add_tran(self, tran):
      """This function adds a transaction to the Book Object and adjusts the balance accordingly."""
      self.tran.append(tran)
      self.balance += tran.amount

class Transaction:
    def __init__(self, ref, kind, amount, date):
        self.ref = ref
        self.kind = kind
        self.amount = amount
        self.date = date

# Functions

def lookup_book(books_list, search= None):
    while True:
        if search:
            for book in books_list:
                if search == book.clave:
                    return book
            print("Clave no encontrada...")        
            search = None
        elif search == "CANCELAR":
            return None
        else:
            print("\n----- Lista de cuentas contables -----\n")
            for book in books_list:
                print("Clave: {} Cuenta Contable: {}".format(book.clave, book.name))
            search = input("Ingrese clave o ingrese CANCELAR")

def new_book(books_list):
    print("\n----- Nueva Cuenta Contable -----\n")
    x = len(books_list)
    if x == 0:
        clave = "0001"
    elif x > 0:
        clave = "000" + str(x)
    elif x >= 9:
        clave = "00" + str(x)
    elif x >= 99:
        clave = "0" + str(x)
    else:
        clave = x
    name = input("Nombre: ")
    i = 0
    for kind in kinds_book:
        i += 1
        print("{}. {}".format(i, kind))
    sel = int(input("Seleccione una opción: ")) - 1
    kind = kinds_book[sel]
    book = Book(clave, name, kind)
    books_list.append(book)
    write_db(books_list, "Books.dat")

def del_book(books_list):
    book = lookup_book(books_list)
    if book:
        books_list.remove(book)
    else:
        print("Eliminación de cuenta contable cancelada...")
    
def new_transaction(books_list):
    ref = input("Referencia para nueva transacción: ")
    i = 0
    for option in kinds_tran:
        i += 1
        print("{}. {}".format(i, option))
    sel = int(input("Seleccione una opcion: ")) - 1
    kind = kinds_tran[sel]
    amount = float(input("Ingrese monto de transacción: $"))
    date = date_input()
    tran = Transaction(ref, kind, amount, date)
    book = lookup_book(books_list)
    if book:
        book.add_tran(tran)
    else:
        print("CANCELADA")




    
