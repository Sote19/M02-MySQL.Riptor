import random
from faker import Faker
from datetime import datetime

# Crear instancia de Faker para generar datos aleatorios
fake = Faker()

#ESTE ES ESPECIAL PARA UNA TIENDA DE ROPA, CAMBIARLO CON VUESTROS PRODUCTOS Y TABLAS!!!

# Lista de valores para generar datos aleatorios
motivo_dev = ["Talla incorrecta", "Color no coincidente con la descripción", "Defecto de fabricación", "Producto dañado durante el envío", "Estilo o diseño no conforme a lo esperado", "Material de baja calidad", "No se ajusta correctamente", "Cambio de opinión del cliente", "Problemas de costura", "No corresponde con la imagen en línea"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Función para generar una fecha de nacimiento aleatoria
def fecha_devolucion():
    fecha = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return fecha.strftime('%d-%m-2023')

# Generar el INSERT con los 5000 registros
insert = "INSERT INTO Devolucion (fecha_dev, motivo_dev) VALUES\n"

for i in range(15):
    uno = valor_aleatorio(motivo_dev)
    fechadev = fecha_devolucion()
    
    # Agregar los valores al INSERT
    insert += f"('{fechadev}', {uno}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
