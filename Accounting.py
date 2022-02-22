# Accounting Module

# Imports

from Essentials import *

# Variables

kinds_tran = ["PAGO", "GASTO"]
kinds_book = [""]
# Classes

class Book:
    def __init__(self, name, kind):
        self.name = name
        self.tran = []
        self.balance = 0
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

def new_transaction():
    ref = input("Referencia para nueva transacción: ")
    
