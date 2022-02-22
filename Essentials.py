# This File Contains Essential Functions for multiple programs
import pickle as pkl
import datetime as dt

def CLS():
    # Clears Terminal Screen
    print("\n" * 50)

def user_input(x, y):
    # Prompts user for y type input with x prompt
    z = 0
    while True:
        try:
            if y == 0:
                z = input(x)
            elif y == 1:
                z = int(input(x))
            else:
                print("ERROR RMM-0001 - WRONG TYPE IN USER_INPUT FUNCTION")
            return z
        except ValueError:
            print("Valor inaceptable intente nuevamente...")

def write_db(object, file_name):
    with open(file_name, "wb") as file:
        pkl.dump(object, file)

def load_db(file_name):
    try:
        with open(file_name, "rb") as file:
            data = pkl.load(file) 
    except FileNotFoundError:
        z = []
        print("Archivo {} no encontrado. Creando nuevo archivo".format(file_name))
        with open(file_name, "wb") as file:
            pkl.dump(z, file)
    finally:
        with open(file_name, "rb") as file:
            data = pkl.load(file)
        return data

def confirm_data():
    print("\n1. Confirmar\n2. Cancelar")
    x = int(input("Seleccione la opción deseada: "))
    if x == 1:
        return True
    else:
        return

def date_input():
    dd = int(input("Día: "))
    mm = int(input("Mes: "))
    yyyy = int(input("Año: "))
    date = dt.date(yyyy, mm, dd)
    return date

def date_between(between_1, between_2, date):
    if date >= between_1 and date <= between_2:
        return True
    else:
        return False