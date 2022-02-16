# Company data file

# Imports

from Essentials import *

# Variable Declarations

# Class Definitions

class Company():
    def __init__(self, name, rs, rfc, dir_fiscal, users, company_prefix):
        self.name = name
        self.rs = rs
        self.rfc = rfc
        self.dir_fiscal = dir_fiscal
        self.users = users
        self.company_prefix = company_prefix
    
    def add_user(self):
        while True:
            while True:
                print("\n----- Nuevo Usuario -----\n")
                name = input('Ingrese iniciales del usuario: ')
                passcode = input('Ingrese contraseña de usuario: ')
                print("\n----- Roles -----\n1. Administrador\n2. Vendedor\n3. Contador\n4. Comprador")
                role = int(input('Seleccione el rol deseado: '))
                roles = {0: "GOD", 1: "Administrador", 2: "Vendedor", 3: "Contador", 4: "Comprador"}
                if role in roles:
                    break
                else:
                    print('Rol inexistente, intente de nuevo...')
            print('Verifique la información: \n\n1.Clave: {}\n2.Contraseña: {}\n3.Rol: {}'.format(name, passcode, roles[role]))
            if confirm_data():
                user = User(passcode, role, name)
                self.users.append(user)

    def del_user(self, search):
        for user in self.users:
            if search == user.name:
                print("Usuario eliminado correctamente.")
                del user
    
    
                

class User():
    def __init__(self, passcode, role, name):
        self.passcode = passcode
        self.role = role
        self.name = name

# Function Definitions

def company_lookup(companies_list, search = False):
    if search:
        while True:
            for company in companies_list:
                if company.name == search:
                    return company
            print("Empresa no existente...")
            return
    else:
        i = 0
        print("\n----- Lista de Empresas -----\n")
        for company in companies_list:
            i += 1
            print("{}. {}".format(i, company.rs))
            

def user_lookup(users_list, search = False):
    if search:
        for user in users_list:
            if user.name == search:
                return user
        return
    else:
        i = 1
        print('\n----- Lista de Usuarios -----\n')
        for user in users_list:
            print("{}. Clave: {} Rol: {}".format(i, user.name, user.role))
            i += 1
        

def new_user(users_list = []):
    while True:
        while True:
            print("\n----- Nuevo Usuario -----\n")
            name = input('Ingrese iniciales del usuario: ')
            passcode = input('Ingrese contraseña de usuario: ')
            print("\n----- Roles -----\n1. Administrador\n2. Vendedor\n3. Contador\n4. Comprador")
            role = int(input('Seleccione el rol deseado: '))
            roles = {0: "GOD", 1: "Administrador", 2: "Vendedor", 3: "Contador", 4: "Comprador"}
            if role in roles:
                break
            else:
                print('Rol inexistente, intente de nuevo...')
        print('Verifique la información: \n\n1.Clave: {}\n2.Contraseña: {}\n3.Rol: {}'.format(name, passcode, roles[role]))
        x = confirm_data()
        if x:
            user = User(passcode, roles[role], name)
            users_list.append(user)
            user_lookup(users_list)
        else:
            print("Intente de nuevo")
            continue
        print('\n1. Ingresar nuevo usuario.\n2. Terminar creación de usuarios')
        confirm = int(input("Seleccione una opción: "))
        if confirm == 1:
            continue
        else:
            return users_list

    
def new_company(companies_list = []):
    print('\n----- Nueva Empresa -----\n')
    name = input("Ingrese Nombre comercial: ")
    rs = input('Ingrese razón social: ')
    rfc = input("Ingrese RFC: ")
    dir_fiscal = input('Ingrese Dirección Fiscal: ')
    company_prefix = input("Ingrese prefijo para facturas y claves de producto: ")
    users = new_user()
    print("\nVerifique que la información de la nueva empresa es correcta:")
    print("1. Nombre: {}\n2. Razón Social: {}\n3. RFC: {}\n4. Dirección Fiscal: {}\n5. Prefijo: {}".format(name, rs, rfc, dir_fiscal, company_prefix))
    user_lookup(users)
    if confirm_data():
        companies_list.append(Company(name, rs, rfc, dir_fiscal, users, company_prefix))
        write_db(companies_list, "Companies.dat")
        return companies_list
    else:
        print('Creación de empresa cancelada...')

def login_company(companies_list):
    while True:
        print("\n----- Inicio -----\n")
        company_lookup(companies_list)
        search = input("Ingrese nombre de empresa:\n")
        company = company_lookup(companies_list, search)
        if company:
            user = input("Usuario: ")
            passcode = input("Contraseña: ")
            for account in company.users:
                if account.name == user and account.passcode == passcode:
                    return company, account
            print("Las credenciales no fueron reconocidas...")
        else:
            continue

