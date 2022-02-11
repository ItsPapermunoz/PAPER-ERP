# This File Contains Essential Functions for multiple programs
import pickle as pkl

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

def write_db(x, y):
    with open(y, "wb") as file:
        pkl.dump(x, file)

def load_db(x):
    y = 0
    try:
        with open(x, "rb") as file:
            y = pkl.load(file) 
    except FileNotFoundError:
        z = []
        print("Archivo {} no encontrado. Creando nuevo archivo".format(x))
        with open(x, "wb") as file:
            pkl.dump(z, file)
    finally:
        with open(x, "rb") as file:
            y = pkl.load(file)
        return y