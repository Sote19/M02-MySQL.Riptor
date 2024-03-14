import random

#ESTE ES ESPECIAL PARA UNA TIENDA DE ROPA, CAMBIARLO CON VUESTROS PRODUCTOS Y TABLAS!!!

# Lista de valores para generar datos aleatorios
talla_chaq = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
capucha_chaq = ["1", "0"]
corte_chaq = ["Entallado", "Regular", "Oversize", "Bomber", "Blazer", "Corte recto", "Corte ajustado", "Corte acolchado", "Corte cruzado", "Corte de motociclista"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 5000 registros
insert = "INSERT INTO Caquetas (talla_chaq, capucha_chaq, corte_chaq) VALUES\n"

for i in range(200):
    talla = valor_aleatorio(talla_chaq)
    capucha = valor_aleatorio(capucha_chaq)
    corte = valor_aleatorio(corte_chaq)    
    
    # Agregar los valores al INSERT
    insert += f"('{talla}', '{capucha}', '{corte}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
