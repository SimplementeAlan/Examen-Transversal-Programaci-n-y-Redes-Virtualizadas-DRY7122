import sqlite3
import hashlib

# Crear/conectar a la base de datos SQLite
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

# Crear tabla de usuarios
c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (nombre TEXT, contraseña TEXT)''')

# Función para almacenar usuarios y contraseñas
def almacenar_usuario(nombre, contraseña):
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    c.execute("INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)", (nombre, hash_contraseña))
    conn.commit()

# Ingresar datos de los usuarios
usuarios = [("Alan", "cisco123"), ("Alvaro", "cisco123"), ("Pedro", "cisco123")]
for usuario in usuarios:
    almacenar_usuario(usuario[0], usuario[1])

# Mostrar datos de la base de datos
c.execute("SELECT * FROM usuarios")
filas = c.fetchall()
for fila in filas:
    print(f"Usuario: {fila[0]}, Hash de Contraseña: {fila[1]}")

# Cerrar la conexión a la base de datos
conn.close()

