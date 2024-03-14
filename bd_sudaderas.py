import random

#ESTE ES ESPECIAL PARA UNA TIENDA DE ROPA, CAMBIARLO CON VUESTROS PRODUCTOS Y TABLAS!!!

# Lista de valores para generar datos aleatorios
talla_suda = ["36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56", "XS", "S", "M", "L", "XL", "XXL", "XXXL"]
capucha_suda = ["1", "0"]
tipobolsillo_suda = ["Canguro", "Bolsillo tipo parche", "Bolsillo tipo ojal", "Bolsillo con cremallera", "Bolsillo tipo cierre magnético", "Bolsillo tipo fuelle", "Bolsillo tipo cierre de botón", "Bolsillo tipo escondido", "Bolsillo tipo divisor", "Bolsillo tipo bolsa interna"]
corte_suda = ["Clásico", "Entallado", "Oversize", "Crop top", "Corte asimétrico", "Corte holgado", "Corte ajustado", "Corte raglán", "Corte cropped", "Corte largo"]
# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 5000 registros
insert = "INSERT INTO Sudaderas (talla_suda, capucha_suda, tipobolsillo_suda, corte_suda) VALUES\n"

for i in range(100):
    uno = valor_aleatorio(talla_suda)
    dos = valor_aleatorio(capucha_suda)
    tres = valor_aleatorio(tipobolsillo_suda)  
    quatro = valor_aleatorio(corte_suda)  
    
    # Agregar los valores al INSERT
    insert += f"('{uno}', '{dos}', '{tres}', '{quatro}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)