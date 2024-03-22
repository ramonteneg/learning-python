from school_db import sqlite3, con, cur 
import os 

status_menu = True
global status_op

def create_countries(op):
    os.system('clear')
    name = input("ingrese el nombre del país:")
    abrev = input("ingrese la abreviatura del país:")
    descrip = input("ingrese una descripción del país:")
    cur.execute("INSERT INTO countries (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", (name, abrev, descrip))
    con.commit()
    print("País creado exitosamente")
    os.system('pause')
    menu()

def create_departments(op):
    os.system('clear')
    name = input("ingrese el nombre del departamento:")
    abrev = input("ingrese la abreviatura del departamento:")
    descrip = input("ingrese la descripción del departamento:")
    cur.execute("SELECT * FROM countries")
    countries = cur.fetchall()
    print(countries)
    id_country = input("Ingrese el ID del país al que pertenece el departamento: ")
    cur.execute("INSERT INTO departments (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_country))
    con.commit()
    print("Departamento creado exitosamente")
    os.system('pause')
    menu()

def create_cities(op):
    os.system('clear')
    name = input("ingrese el nombre de la ciudad: ")
    abrev = input("ingrese la abreviatura de la ciudad: ")
    descrip = input("ingrese la descripción de la ciudad: ")
    cur.execute("SELECT * FROM departments")
    departments = cur.fetchall()
    print(departments)
    id_depart = input("ingrese el id del departamento al que pertenece la ciudad: ")
    cur.execute("INSERT INTO cities (name, abrev, descrip, id_depart, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_depart))
    con.commit()
    print("ciudad creada exitoamente")
    os.system('pause')
    menu()

def create_identification_type(op):
    os.system('clear')
    name = input("ingrese el nombre del tipo de idn: ")
    abrev = input("ngrese la abreviatura de id: ")
    descrip = input("ingrese la descripción del tipo de id: ")
    cur.execute("INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (name, abrev, descrip))
    con.commit()
    print("tipo de identificación creado exitosamente")
    os.system('pause')
    menu()

def create_user(op):
    os.system('clear')
    email = input("ingrese el correo electrónico: ")
    password = input("ingrese la contraseña: ")
    cur.execute("INSERT INTO users (email, password, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (email, password, 0))  # Estado predeterminado
    con.commit()
    print("usuario creado exitosamente")
    os.system('pause')
    menu()

def create_person(op):
    os.system('clear')
    first_name = input("Ingrese el primer nombre de la persona: ")
    last_name = input("Ingrese el apellido de la persona: ")
    cur.execute("SELECT * FROM identification_types")
    identification_types = cur.fetchall()
    print(identification_types) 
    id_ident_type = input("ingrese el id del tipo de identificación de la persona: ")
    ident_number = input("ingrese el número de identificación de la persona: ")
    cur.execute("SELECT * FROM cities")
    cities = cur.fetchall()
    print(cities) 
    id_exp_city = input("ingrese el id de la ciudad de expedición del documento: ")
    address = input("ingrese la dirección de la persona: ")
    mobile = input("ingrese el número de teléfono de la persona: ")
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    print(users)
    id_users = input("ingrese id de usuario de persona: ")
    cur.execute("INSERT INTO persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users))
    con.commit()
    print("datos de persona creados exitosamente.")
    os.system('pause')
    menu()

def create_student(op):
    os.system('clear')
    code = input("ingrese código de estudiante: ")
    cur.execute("SELECT * FROM persons")
    person = cur.fetchall()
    print(person) 
    id_person = input("Ingrese id de persona: ")
    cur.execute("INSERT INTO students (code, id_person, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (code, id_person, 0))  # Estado predeterminado
    con.commit()
    print("datos de estudiante creados exitosamente.")
    os.system('pause')
    menu()

def menu():
    status_opt = True
    while status_menu:
        os.system("clear")
        print("Menu")
        print("[1] Create countries")
        print("[2] Create department")
        print("[3] Create city")
        print("[4] Create identification type")
        print("[5] Create user")
        print("[6] Create person")
        print("[7] Create student")
        print("[8] Exit")

        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print("Opción invalida, intente de nuevo")
            else :
                status_opt = False

        if opt == '1':
            create_country(opt)
        elif opt == '2':
            create_department(opt)
        elif opt == '3':
            create_city(opt)
        elif opt == '4':
            create_identification_type(opt)
        elif opt == '5':
            create_user(opt)
        elif opt == '6':
            create_person(opt)
        elif opt == '7':
            create_student(opt)
        else:
            print("Hasta pronto")
            exit()
            
menu()
con.close()