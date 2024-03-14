import random
from faker import Faker

# Crear instancia de Faker para generar datos aleatorios
fake = Faker()

# Lista de valores para generar datos aleatorios
contacto_prov = ["María López", "Juan Martínez", "Laura Sánchez", "Carlos Fernández", "Andrea Rodríguez", "Sergio González", "Ana Pérez", "Pablo Díaz", "Marta García", "Alejandro Ruiz", "Paula Torres", "Javier Moreno", "Lucia Navarro", "Diego Jiménez", "Elena Ramírez", "Daniel Ortiz", "Carmen Castro", "Marcos Herrera", "Sara Medina", "Adrián Castro"]
nombre_prov = ["ModaStyle Distribuciones", "Tendencia Textil S.A.", "FashionEmporium Proveedores", "UrbanChic Suministros", "Elegance Couture Producers", "TrendyThreads Wholesale", "ModaVanguardia Distribución", "StyleFusion Suministros", "VogueVentures S.A.", "FashionForward Supplies", "GlamourGrove Proveedores", "CoutureConnect Distribuciones", "StreetStyle Trading Co.", "ChicWear Wholesale", "ModaExclusiva Distribución", "TrendyTrove Suministros", "CoutureCrafters S.A.", "UrbanEdge Suppliers", "FashionFocus Distribuciones", "StyleSavvy Wholesale"]
direccion_prov = ['123 Calle Principal', '456 Avenida Central', '789 Calle Secundaria', '10 Avenida Norte', '24 Calle Este', '567 Calle Oeste', '890 Avenida Sur', '135 Calle Norte', '246 Avenida Este', '579 Calle Central', '802 Avenida Principal', '153 Calle Secundaria', '364 Avenida Norte', '697 Calle Este', '910 Avenida Oeste', '246 Calle Sur', '579 Avenida Norte', '802 Calle Este', '135 Avenida Sur', '468 Calle Oeste']

# Función para generar un número de teléfono aleatorio
def telefonos():
    return fake.random_number(digits=9)

# Generar el INSERT con los 20 registros
insert = "INSERT INTO Proveedor (contacto_prov, nombre_prov, telefono_prov, direccion_prov, electronico_prov) VALUES\n"

for i in range(20):
    uno = contacto_prov.pop()
    dos = nombre_prov.pop()
    telefono = telefonos()
    tres = direccion_prov.pop()
    quatro = fake.email()  
    
    # Agregar los valores al INSERT
    insert += f"('{uno}', '{dos}', '{telefono}', '{tres}', '{quatro}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
