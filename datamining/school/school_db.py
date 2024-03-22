
import sqlite3

create a database connection (database name)
con = sqlite3.connect('school.db')

cur = con.cursor()

cur.execute('''
   CREATE TABLE IF NOT EXISTS countries(
        id_country INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, abrev VARCHAR(10) NOT NULL, descrip VARCHAR(10) NOT NULL,
		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, deleted_at DATETIME DEFAULT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS identification_types (
        id_ident_type INTEGER PRIMARY KEY, name VARCHAR(50) NOT NULL, abrev VARCHAR(10) NOT NULL, descrip VARCHAR(100) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, deleted_at DATETIME DEFAULT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id_users INTEGER PRIMARY KEY NOT NULL, email VARCHAR(100) NOT NULL, password VARCHAR(250) NOT NULL, status INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, deleted_at DATETIME DEFAULT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id_department INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, abrev VARCHAR(10) NOT NULL, descrip VARCHAR(10) NOT NULL,
        id_country INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_country) REFERENCES countries(id_country)
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id_exp_city INTEGER PRIMARY KEY, name VARCHAR(50) NOT NULL, abrev VARCHAR(10) NOT NULL, descrip VARCHAR(100) NOT NULL,
        id_depart INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_depart) REFERENCES departments(id_department)  
    )
''')



cur.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        id_persons INTEGER PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50), id_ident_type INTEGER,
        ident_number VARCHAR(15) NOT NULL, id_exp_city INTEGER, address VARCHAR(150) NOT NULL, mobile VARCHAR(50) NOT NULL,
        id_users INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_ident_type) REFERENCES identification_types(id_ident_type),
        FOREIGN KEY (id_exp_city) REFERENCES cities(id_exp_city),
        FOREIGN KEY (id_users) REFERENCES users(id_users)
       
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id_student INTEGER PRIMARY KEY NOT NULL, code VARCHAR(50) NOT NULL, id_person INTEGER,status INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_persons) REFERENCES Persons(id_persons)
    )
''')

con.commit()

print("La base de datos fue creada exitosamente")

