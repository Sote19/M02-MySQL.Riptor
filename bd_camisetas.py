import random

#ESTE ES ESPECIAL PARA UNA TIENDA DE ROPA, CAMBIARLO CON VUESTROS PRODUCTOS Y TABLAS!!!

# Lista de valores para generar datos aleatorios
talla_cami = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
corte_cami = ["Ajustado", "Regular", "Holgado", "Corte en V", "Cuello redondo", "Cuello en pico", "Sin mangas", "Manga corta", "Manga larga", "Manga raglán"]


# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 5000 registros
insert = "INSERT INTO Camisetas (talla_cami, corte_cami) VALUES\n"

for i in range(250):
    talla = valor_aleatorio(talla_cami)
    corte = valor_aleatorio(corte_cami)
    
    # Agregar los valores al INSERT
    insert += f"('{talla}', '{corte}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
