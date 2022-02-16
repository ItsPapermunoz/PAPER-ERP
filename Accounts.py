# Imports

from re import template
from Essentials import *
from Company_data import *
# Variable Declarations


# Class Definitions

class Account():
    def __init__(self, clave, name, rs, rfc, saldo, dias_credito, limite_credito, clas, 
    status, dir_fiscal, dir_entrega, contact, executive):
        self.clave = clave
        self.name = name
        self.rs = rs
        self.rfc = rfc
        self.saldo = saldo
        self.dias_credito = dias_credito
        self.limite_credito = limite_credito
        self.clas = clas
        self.status = status
        self.dir_fiscal = dir_fiscal
        self.dir_entrega = dir_entrega
        self.contact = contact
        self.executive = executive

class Contact():
    def __init__(self, name, phone, email, title):
        self.name = name
        self.phone = phone
        self.email = email
        self.title = title
# Function Definitions

def new_contact(contacts_list):
    while True:
        print("\n----- Nuevo Contacto -----\n")
        name = input("Nombre y Apellido: ")
        phone = input("Teléfono: ")
        email = input("Correo electrónico: ")
        title = input("Titulo: ")
        print("\nVerifique que la información es correcta:\n1.Nombre: {}\n2.Teléfono: {}\n3.Correo: {}\n4.Titulo: {}".format(name, phone, email, title))
        confirm = int(input("Si la información es correcta, ingrese 1 de lo contrario ingrese 0: "))
        if confirm == 1:
            contact = Contact(name, phone, email, title)
            contacts_list.append(contact)
            write_db(contacts_list, "Contacts.dat")
            return contact
        
def new_account(clients_list, contacts_list):
    print("\n-----Nuevo Cliente-----\n")
    while True:
        x = len(clients_list) + 1
        if x == 1:
            clave = "0001"
        elif x >= 2:
            clave = "000{}".format(x)
        elif x >= 10:
            clave = "00{}".format(x)
        elif x >= 100:
            clave = "0{}".format(x)
        else:
            clave = str(x)
        name = input("Ingrese apodo de nuevo cliente:\n")
        rs = input("Ingrese razón social de nuevo cliente:\n")
        rfc = input("Ingrese RFC de nuevo cliente:\n")
        dir_fiscal = input("Ingrese dirección fiscal del nuevo cliente: ")
        dir_entrega = input("Ingrese dirección de entrega del nuevo cliente o ingrese \"IGUAL\" para seleccionar la misma dirección que la fiscal: ")
        if dir_entrega == "IGUAL":
            dir_entrega = dir_fiscal
        contact = new_contact(contacts_list)
        saldo = int(input("Ingrese Saldo del nuevo cliente:\n"))
        dias_credito = -1
        while dias_credito < 0:
            dias_credito = int(input("Ingrese días de crédito autorizados: "))
            if dias_credito > 0:
                limite_credito = int(input("Ingrese limite de crédito autorizado: "))
            elif dias_credito < 0:
                print("Días de crédito no puede ser menor a 0...")
            else:
                limite_credito = 0
        clas = input("Ingrese Clasificación de cliente: ")
        status = "Activo"
        executive = input("Ingrese la Clave del vendedor asignado: ")
        new_account = Account(clave, name, rs, rfc, saldo, dias_credito, limite_credito, clas, status, dir_fiscal, dir_entrega, contact, executive)
        print("\nVerifique la información de su nuevo cliente:\nCLAVE: {}\nApodo: {}\nRazón Social: {}\nRFC: {}".format(clave, name, rs, rfc))
        print("Dirección Fiscal: {}\nDirección de entrega: {}\n\n---Crédito y Cobranza---\n".format(dir_fiscal, dir_entrega))
        print("Saldo inicial: ${}\nDías de crédito: {}\nLímite de crédito: ${}".format(saldo, dias_credito, limite_credito))
        y = user_input("\n1. La información es correcta\n2.Corregir información\n3.Cancelar alta de cliente\n", 1)
        if y == 1:
            print("\nAlta de cliente {} exitosa.\n".format(name)) 
            clients_list.append(new_account)
            write_db(clients_list, "Clients.dat")
            return clients_list
        elif y == 2:
            print("\n")
            continue
        else:
            print("Alta de cliente cancelada.")
            break
        
def lookup_client(clients_list, lookup = 0, search = None):
    i = 1
    temp_list = []
    if lookup == 0:
        print("\n ----- Lista de Clientes -----\n ")
        for client in clients_list:
            print("{}. Clave: {} Nombre: {} Contacto: {}".format(i, client.clave, client.name, client.contact.name))
            i += 1
            temp_list.append(client)
    if lookup == 1:
        for client in clients_list:
            if client.clave == search:
                print("{}. Clave: {} Nombre: {} Contacto: {}".format(i, client.clave, client.name, client.contact.name))
                return client
        print("Clave no registrada")
        return None
    elif lookup == 2:
        for client in clients_list:
            if client.clas == search:
                temp_list.append(client)
                print("{}. Clave: {} Nombre: {} Contacto: {}".format(i, client.clave, client.name, client.contact.name))
        if len(temp_list) > 0:
            return temp_list
        else:
            print("No hay ninguna cuenta con la clasificación {}".format(search))
            return None




def del_client(clients_list):
    x = input("Ingrese la clave del cliente a eliminar.\n")
    i = 0
    for client in clients_list:
        if x == client.clave:
            del clients_list[i]
            print("Cliente {} eliminado exitosamente.".format(client.rs))
        i += 1
    write_db(clients_list, "Clients.dat")
    return clients_list

# Main




    