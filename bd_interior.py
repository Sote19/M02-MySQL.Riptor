import random

#ESTE ES ESPECIAL PARA UNA TIENDA DE ROPA, CAMBIARLO CON VUESTROS PRODUCTOS Y TABLAS!!!

# Lista de valores para generar datos aleatorios
talla_lenceria_inter = ["XS", "S", "M", "L", "XL", "XXL", "XXXL", "34", "36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56"]
conjunto_inter = ["1", "0"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 50 registros
insert = "INSERT INTO Ropa_interior (talla_lenceria_inter, conjunto_inter) VALUES\n"

for i in range(50):
    talla = valor_aleatorio(talla_lenceria_inter)
    conjunto = valor_aleatorio(conjunto_inter)
    
    # Agregar los valores al INSERT
    insert += f"('{talla}', '{conjunto}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
