import random
from faker import Faker
from datetime import datetime

# Crear instancia de Faker para generar datos aleatorios
fake = Faker()

# Función para generar una fecha de nacimiento aleatoria
def fecha_nacimiento():
    fecha = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return fecha.strftime('%Y-%m-%d')

# Función para generar un número de teléfono aleatorio
def telefonos():
    return fake.random_number(digits=9)

# Función para generar 10 letras
def contras():
    return fake.text(max_nb_chars=10)

# Generar los 500 registros
registros = []
for i in range(500):
    nombre = fake.first_name()
    apellidos = fake.last_name()
    pais = fake.country()
    ciudad = fake.city()
    cp = fake.random_number(digits=5)
    direccion = fake.address()
    telefono = telefonos()
    correo = fake.email()
    fechanac = fecha_nacimiento()
    estilo = fake.random_element(elements=("Clásico", "Deportivo", "Casual", "Elegante"))
    contraseña = contras()
    ocupacion = fake.job()
    
    # Agregar los valores al registro sin intros
    registros.append(f"('{nombre}', '{apellidos}', '{pais}', '{ciudad}', {cp}, '{direccion}', {telefono}, '{correo}', '{fechanac}', '{estilo}', '{contraseña}', '{ocupacion}')")

# Construir el INSERT con los registros sin intros
insert = f"INSERT INTO Usuarios (nombre_usu, apellidos_usu, pais_usu, ciudad_usu, cp_usu, direccion_usu, telf_usu, correo_usu, fechanac_usu, estilo_usu, contraseña_usu, ocupacion_usu) VALUES "
insert += ", ".join(registros) + ";"

# Imprimir el INSERT generado sin intros
print(insert)
